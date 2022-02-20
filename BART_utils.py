import pandas as pd
import numpy as np
import json
from collections import Counter
from itertools import chain, repeat
from tqdm import tqdm
from load_data import *
import matplotlib.pyplot as plt
import streamlit as st

tqdm.pandas()

import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-mnli")
nli_model = (
    AutoModelForSequenceClassification.from_pretrained(
        "facebook/bart-large-mnli"
    ).cuda()
    if torch.cuda.is_available()
    else AutoModelForSequenceClassification.from_pretrained("facebook/bart-large-mnli")
)


def get_prob(sequence, label):
    premise = sequence
    hypothesis = f"This example is {label}."

    # run through model pre-trained on MNLI
    x = tokenizer.encode(
        premise, hypothesis, return_tensors="pt", truncation_strategy="only_first"
    )
    logits = nli_model(x.to(device))[0]

    # we throw away "neutral" (dim 1) and take the probability of
    # "entailment" (2) as the probability of the label being true
    entail_contradiction_logits = logits[:, [0, 2]]
    probs = entail_contradiction_logits.softmax(dim=1)
    prob_label_is_true = probs[:, 1]
    return prob_label_is_true[0].item()


def judge_mbti(sequence, labels):
    out = []
    for l in labels:
        temp = get_prob(sequence, l)
        out.append((l, temp))
    out = sorted(out, key=lambda x: x[1], reverse=True)
    return out


def compute_score(text, type):
    x, y = type.split("_")
    x_score = np.sum([i[1] for i in judge_mbti(text, keywords_en[type][x])])
    y_score = np.sum([i[1] for i in judge_mbti(text, keywords_en[type][y])])

    if x_score > y_score:
        choice = x
        score = x_score
    else:
        choice = y
        score = y_score

    x_score_scaled = (x_score / (x_score + y_score)) * 100
    y_score_scaled = (y_score / (x_score + y_score)) * 100

    stat = {x: x_score_scaled, y: y_score_scaled}

    return choice, stat


def mbti_translator(text):
    E_I = compute_score(text, "E_I")
    N_S = compute_score(text, "N_S")
    T_F = compute_score(text, "T_F")
    P_J = compute_score(text, "P_J")

    return (E_I[0] + N_S[0] + T_F[0] + P_J[0]), (E_I[1], N_S[1], T_F[1], P_J[1])


def plot_mbti(result):
    fig, ax = plt.subplots(figsize=(10, 5))

    start = 0
    x, y = result.values()
    x_type, y_type = result.keys()

    ax.broken_barh([(start, x), (x, x + y)], [10, 9], facecolors=("#FFC5BF", "#D4F0F0"))
    ax.set_ylim(5, 15)
    ax.set_xlim(0, 100)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.set_yticks([15, 25])
    ax.set_xticks([0, 25, 50, 75, 100])

    ax.text(x - 6, 14.5, x_type + " :" + str(int(x)) + "%", fontsize=15)
    ax.text((x + y) - 6, 14.5, y_type + " :" + str(int(y)) + "%", fontsize=15)

    st.pyplot(fig)
