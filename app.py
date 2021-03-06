import streamlit as st


from BART_utils import get_prob, judge_mbti, compute_score, mbti_translator, plot_mbti


st.title("MBTI ë²ì­ê¸°")
st.header("ð»ëë ì¤ë ì´ë¤ MBTIì²ë¼ ë§íê³ , ì´ììê¹?")
st.write("ð¤ë¬¸ì¥ì ìë ¥íë©´, ì´ë¥¼ ë¶ìí´ì MBTIë¥¼ ì¶ë ¥í´ì¤ëë¤ð¤ ìì§ì ìì´ë§ ì§ìë©ëë¤!")

user_input = st.text_input("ððë¬¸ì¥ì ìë ¥íë©´ MBTIê° ëìµëë¤!", "I stayed home all day")

submit = st.button("ë¬¸ì¥ ìì±")


if submit:

    output_mbti, output_ratio = mbti_translator(user_input)
    st.success("Success")

    st.subheader("ð¤ì°¸ ì´ MBTIê°ì ë¬¸ì¥ì´êµ°ìð : " + output_mbti)

    for result in output_ratio:
        plot_mbti(result)
