
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import pandas as pd
import os

# Loading api key
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

def upload_excel(file_path):
    # Carregar a base de chamados
    df = pd.read_excel(file_path)

    # Selecionar as colunas relevantes para a busca
    features = ['Sintoma', 'Descrição', 'Resolução']

    # Combinar as features em uma única coluna de texto
    df['texto'] = df[features].apply(lambda x: ' '.join(x.astype(str)), axis=1)

    # Criar documentos a partir dos dados
    documents = [
        {"source": row["Número"], "content": row["texto"]} for _, row in df.iterrows()
    ]

    # Dividir os documentos em chunks menores
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100
    )

    documents = text_splitter.create_documents([(f'{d["source"]} - {d["content"]}') for d in documents])

    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    persist_directory = 'db_csv'

    # Criar um vetor store 
    db_csv = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_directory
    )
