from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
import google.generativeai as genai
import os

genai.configure(api_key=api_key)

# 1. Carregar documentos do diretório
documents = []

pdf_loader = PyPDFLoader('./test/Anúbis.pdf')
loaded_documents = pdf_loader.load()

for i, page_content in enumerate(loaded_documents):
  documents.append(Document(
      page_content=page_content.page_content,
      metadata={"source": f'./test/Anúbis.pdf - Página {i+1}'}
  ))

# 3. Criar embeddings dos textos
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    task_type='retrieval_document',
    google_api_key=api_key
)
# Embed documentos, não textos
vector = embeddings.embed_documents([doc.page_content for doc in documents])

persist_directory = 'db_google'

my_database = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=persist_directory
)

# 4. Instanciar o modelo de linguagem (Gemini)
llm = GoogleGenerativeAI(
    model='gemini-1.0-pro',
    temperature=0.0,
    max_output_tokens=800,
    google_api_key=api_key
)

# Defining the conversational memory
retaining_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

# 5. Criar a cadeia de RAG
chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=my_database.as_retriever(),
    memory=retaining_memory
)

# 6. Fazer perguntas e obter respostas
query = input("Pergunta: ")
result = chain.invoke({"question": query})
print(result['answer'])