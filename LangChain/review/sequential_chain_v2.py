import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

# .env 파일에서 환경 변수 로드
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ChatOpenAI 모델 초기화
# Temperature 설정(모델의 응답 다양성 조절)
openai_llm = ChatOpenAI(model="gpt-5-mini", api_key=OPENAI_API_KEY, temperature=0.7)

# --- Prompt template define ---
# Prompt 1: review translate
prompt1 = PromptTemplate(
    input_variables=['review'],
    template="다음 숙박 시설 리뷰를 한글로 번역하세요.\n\n{review}"
)

# Prompt 2: Translated review summary
prompt2 = PromptTemplate.from_template(
    "다음 숙박 시설 리뷰를 한 문장으로 요약하세요.\n\n{translation}"
)

# Prompt 3: Translated review rating
prompt3 = PromptTemplate.from_template(
    "다음 숙박 시설 리뷰를 읽고 0점 부터 10점 사이에서 부정/긍정 점수를 매기세요. 숫자만 대답하세요.\n\n{translation}"
)

# Prompt 4: Detect language form review
prompt4 = PromptTemplate.from_template(
    "다음 숙박 시설 리뷰에 사용된 언어가 무엇인가요? 언어 이름만 답하세요.\n\n{review}"
)

# Prompt 5: Make reply (Original review language)
prompt5 = PromptTemplate.from_template(
    "다음 숙박 시설 리뷰 요약에 대해 공손한 답변을 작성하세요. \n답변언어:{language}\n리뷰요약:{summary}"
)

# Prompt 6: Reply translate to Korean
prompt6 = PromptTemplate.from_template(
    "다음 생성된 답변을 한국어로 번역해주세요. \n 리뷰 번역{reply1}"
)

# --- LCEL을 사용한 체인 구성 요소 정의 ---
# 각 단계는 '프롬프트 | LLM | 출력 파서'의 형태로 구성됨.
# step 1: 리뷰 번역 체인
translate_chain_component = prompt1 | openai_llm | StrOutputParser()

# step 2: 번여
translate_chain_component = prompt1 | openai_llm | StrOutputParser()

translate_chain_component = prompt1 | openai_llm | StrOutputParser()

translate_chain_component = prompt1 | openai_llm | StrOutputParser()

translate_chain_component = prompt1 | openai_llm | StrOutputParser()

translate_chain_component = prompt1 | openai_llm | StrOutputParser()