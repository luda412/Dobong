from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI
from langchain_classic import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
load_dotenv()

# 제목
st.title("ChatPDF")
st.write("---")

# 파일 업로드
uploaded_file = st.file_uploader("PDF 파일을 올려주세요!", type=['pdf'])
st.write("---")

def pdf_to_document(uploaded_file):
    temp_dir = tempfile.TemporaryDirectory()
    temp_filepath = os.path.join(temp_dir.name, uploaded_file.name)
    with open(temp_filepath, "wb") as f:
        f.write(uploaded_file.getvalue())
    loader = PyPDFLoader(temp_filepath)
    pages = loader.load_and_split()
    return pages

# 업로드된 파일 처리
if uploaded_file is not None:
    pages = pdf_to_document(uploaded_file)

    # Splitter
    # 페이지 단위로 분할한 문서를 의미있는 정보 덩어리인 청크로 분할
    # 그 중, recursive로 인해서 문자리스트인 \n\n, \n, 쉼표, 공백으로 문서를 분할함.
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size = 300,
        chunk_overlap = 20,
        length_function = len,
        # 구분자를 문자열로 해석
        is_separator_regex=False,
    )
    # 페이지 단위로 분할된 문서를 청크 단위로 분할한 후 그 리스트를 texts에 담음
    texts = text_splitter.split_documents(pages)

    # Embedding
    # 문서에서 연관된 정보를 추출하기 위해 임베딩 시 사용할 모델을 선택
    embeddings_model = OpenAIEmbeddings(
        model="text-embedding-3-large",
        # With the `text-embedding-3` class
        # of models, you can specify the size
        # of the embedding you want returned.
        # dimensions=1024
    )

    # Chroma DB
    # 벡터DB에 청크 단위로 분할된 문서 리스트 및 임베딩 모델 전달
    db = Chroma.from_documents(texts, embeddings_model)

    # User Input
    st.header("PDF에게 질문해보세요!!")
    question = st.text_input("질문을 입력하세요.")
    
    if st.button("질문하기"):
        with st.spinner("Wait for it..."):
            # Retriever
            # 체인을 형성하여 프롬프트를 전달할 GPT 모델 불러와서 temperature를 0으로 창의성을 배제 시킴
            llm = ChatOpenAI(temperature=0)
            # 벡터 저장소에 대한 retriever 인스턴스 생성(DB 관련 인스턴스), llm 인스턴스 전달
            retriever_from_llm = MultiQueryRetriever.from_llm(
                retriever = db.as_retriever(), llm=llm
            )

            # Prompt Template
            # hub를 이용하여 공개되어있는 prompt 사용
            prompt = hub.pull("rlm/rag-prompt")

            # Generate
            # 검색된 문서를 합쳐주는 함수
            def format_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)
            # 체인 생성
            # context에 검색된 문서를 결합한 결과(retriever_from_llm | format_docs)를, question에 사용자 질문(RunnablePassthrough)을 전달
            rag_chain = (
                {"context": retriever_from_llm | format_docs, "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
            )

            # Question
            result = rag_chain.invoke(question)
            st.write(result)

