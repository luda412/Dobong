from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# Loader
loader = PyPDFLoader("LangChain/chatPDF/unsu.pdf")
pages = loader.load_and_split()

# Splitter
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 300,
    chunk_overlap = 20,
    length_function = len,
    is_separator_regex=False,
)

texts = text_splitter.split_documents(pages)

# Embedding
embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
    # With the `text-embedding-3` class
    # of models, you can specify the size
    # of the embedding you want returned.
    # dimensions=1024
)

# Chroma DB
db = Chroma.from_documents(texts, embeddings_model)

# Retriever
question = "아내가 먹고 싶어하는 음식은 무엇이야?"
llm = ChatOpenAI(temperature=0)

retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever = db.as_retriever(), llm=llm
)
docs = retriever_from_llm.invoke(question)
print(len(docs))
print(docs)