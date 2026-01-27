from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 프롬프트 정의, 해당 템플릿은 리뷰와 점수 범위를 입력 받아 AI 평가 생성을 도움
prompt_template = "이 음식 리뷰 '{review}'에 대해 '{rating1}'점부터 '{rating2}'점까지의 평가를 해주세요."
prompt = PromptTemplate(
    input_variables=["review", "rating1", "rating2"], template=prompt_template
)

# 모델 초기화
openai = ChatOpenAI(model="gpt-5-mini", api_key=OPENAI_API_KEY, temperature=0.7)

# 프롬프트, llm, 출력 파서 연결
chain = prompt | openai | StrOutputParser()

try:
    response = chain.invoke({
        "review": "맛은 있엇지만 배달 포장이 부족하여 아쉬웠습니다.",
        "rating1": "1",
        "rating2": "5"
    })
    print(f"평가 결과: {response}")
except Exception as e:
    print(f"Error: {e}")