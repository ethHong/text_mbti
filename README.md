# Text to MBTI (Zero Shot - model)
😄 재미로 만드는 MBTI 해석기 - MBTI Translator (나는 오늘 어떤 MBTI처럼 살았을까?)

## About the project & Examples
* 문장을 입력하세요! 다능하다면 '성격유형' 의 성향이 드러날만한 문장을 입력하세요. 아래와 같이 어떤 성격유형에 가까운 발화인지 출력합니다
```
Input: "I stayed home all day"

===

Output:

You are:  ISFP
Ratio {'E': 27.338588094108168, 'I': 72.66141190589182} {'N': 22.149243913056992, 'S': 77.85075608694301} {'T': 46.17274433748438, 'F': 53.82725566251562} {'P': 57.30466611213056, 'J': 42.69533388786944}
```

```
Input: "I'm making plans for my trip to Osaka. I'm so excited!"

===

Output:

You are:  ESTJ
Ratio {'E': 71.53464326345417, 'I': 28.46535673654582} {'N': 35.33135528913844, 'S': 64.66864471086156} {'T': 58.70273162646018, 'F': 41.29726837353982} {'P': 46.96476087995551, 'J': 53.03523912004449}
```

## Model and requirements
* 사용 모델: https://huggingface.co/facebook/bart-large-mnli
* Huggingface 에 공유된 Facebook 으 Zero-shot text classification 모델을 사용합니다. 
* torch 및 transformers 세팅이 필요하며, 아래와 같이 pipenv 를 설정해주세요 - ~~pipfile을 통해 설치 가능합니다.
* >> 02.20 update: Streamlit Sharing을 통한 데모 배포를 위해 requirement.txt만을 사용합니다

```
pip install -r requirements.txt
```

다만, torch 및 transformers 는 별도 환경설정이 필요할 수 있습니다. 
* 여기에서 각 환경에 맞는 pytorch 를 설정해주세요: https://pytorch.org
```
pip install transformers
```
Zero-shot model 에 대한 레퍼런스는 https://joeddav.github.io/blog/2020/05/29/ZSL.html 이 링크를 참고해주세요!

## Module Description 
Zero-shot text classification은, 텍스트르 input으로 받아, 입력된 label 들과 관련된 주제일 확률을 output합니다. 
이를 활용해, MBTI의 각 요소들과 관련된 단어들을 JSON형태로 입력해 비교한 뒤, MBTI 를 출력해줍니다. 

## Plans
* 아직은 ipynb 로, 간단히 데모만 만들어놓은 상황입니다.
* 추후 MBTI-dictionary 를 업데이트해, 정확도롸 설득력을 올리는 작업을 할 예정입니다. 
* MT (machine translation) 을 이용한 중역 및, 카카오브레인 오픈소스 zero-shot model 등을 활용해 한국어에 대한 지원을 확대해볼 예정입니다. 
