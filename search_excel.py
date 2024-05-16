from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Loading api key
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

def search_excel(query):
    # Criar embeddings usando OpenAI
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    persist_directory = 'db_csv'

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

    # Prepare database for search
    db_excel = Chroma(
        persist_directory=persist_directory, 
        embedding_function=embeddings)

    # Criar uma cadeia de recuperação QA
    question_answering = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=db_excel.as_retriever(),
        memory=retaining_memory
    )

    answer = question_answering.invoke({"question": "Answer in brazilian portuguese and only with information that is in the documents provided." + query})
    result = answer['answer']

    return result