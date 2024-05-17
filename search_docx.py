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

def search_docx(query):
    # Criar embeddings usando OpenAI
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    # Diretório da base de embeddings
    persist_directory = 'db_docx'

    # Cria o LLM
    llm = ChatOpenAI(
        openai_api_key= api_key,
        model_name='gpt-3.5-turbo',
        temperature=0.0
    )

    # Memória da conversa
    retaining_memory = ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=5,
        return_messages=True
    )

    # Prepara a base para consulta
    db_docx = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    # Criar uma cadeia de recuperação QA
    question_answering = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=db_docx.as_retriever(),
        memory=retaining_memory
    )

    # Mostra resposta
    answer = question_answering.invoke({"question": "Answer in brazilian portuguese and only with information that is in the documents provided." + query})
    result = answer['answer']

    # Mostra fonte utilizada para a resposta
    results = db_docx.similarity_search_with_relevance_scores(query, k=1)
    if len(results) == 0 or results[0][1] < 0.7:
        sources = "Não foram encontradas fontes."
    else:
        sources = [doc.metadata.get("source", None) for doc, _score in results]

    return result, sources