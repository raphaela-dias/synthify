from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_openai import ChatOpenAI
import pandas as pd
from dotenv import load_dotenv
import os

# Loading api key
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

# Carregar a base de chamados
df = pd.read_excel("test\Base Chamados_V1.xlsx")

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
    chunk_overlap=100)

documents = text_splitter.create_documents([d["content"] for d in documents])

# Criar embeddings usando OpenAI
embeddings = OpenAIEmbeddings()

persist_directory = 'db_csv'

# Criar um vetor store 
db_csv = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=persist_directory
)

# Criar um modelo de linguagem OpenAI
llm = ChatOpenAI(
    openai_api_key= api_key,
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

# Defining the conversational memory
retaining_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

# Criar uma cadeia de recuperação QA
qa = question_answering = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=db_csv.as_retriever(),
    memory=retaining_memory
)

# Exemplo de uso
query = input("Escreva qual o problema que deseja resolver: ")

# Obter resposta da cadeia QA
result = qa.invoke({"question": "Answer in brazilian portuguese and only with information that is in the documents provided." + query})

# Imprimir a resposta
print(result['answer'])