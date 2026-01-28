from langchain_community.document_loaders import PyPDFLoader

# Loader
loader = PyPDFLoader("chatPDF/unsu.pdf")
pages = loader.load_and_split()

print(pages[0])