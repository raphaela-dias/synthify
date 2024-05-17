
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import pandas as pd
import os

# Carrega API key
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

def upload_excel(file_path):
    # Carrega o arquivo .excel
    df = pd.read_excel(file_path)

    # Seleciona as colunas relevantes para a busca
    features = ['Sintoma', 'Descrição', 'Resolução']

    # Combina as features em uma única coluna de texto
    df['texto'] = df[features].apply(lambda x: ' '.join(x.astype(str)), axis=1)

    # Cria documentos a partir dos dados
    documents = [
        {"source": row["Número"], "content": row["texto"], "metadata": {"filename": file_path}} for _, row in df.iterrows()
    ]

    # Divide os documentos em chunks menores
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100
    )

    documents = text_splitter.create_documents([(f'{d["source"]} - {d["content"]} - {d["metadata"]}') for d in documents])

    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    persist_directory = 'db_excel'

    # Cria um vetor store 
    db_excel = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_directory
    )


def upload_docx(file_path):
    #Lista de chunks
    documents = []

    # Carrega arquivo .docx
    xml_loader = Docx2txtLoader(file_path)
    document = xml_loader.load()

    # Divide os documentos em chunks menores
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  
        chunk_overlap=100
    )
    split_docs = text_splitter.split_documents(document)

    # Adiciona os chunks na lita documents
    documents.extend(split_docs)

    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    persist_directory = 'db_docx'

    #Cria um vetor store
    db_docx = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=persist_directory
)

