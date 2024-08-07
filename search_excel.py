from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import ast
import os

# Carrega a API key
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

def search_excel(query):
    # Criar embeddings usando OpenAI
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    # Diretório da base de embeddings
    persist_directory = 'db_excel'

    # Cria o LLM
    llm = ChatOpenAI(
        openai_api_key=api_key,
        model_name='gpt-3.5-turbo',
        temperature=0.0
    )

    # Memória de conversa
    retaining_memory = ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=5,
        return_messages=True
    )

    # Prepara a base para consulta
    db_excel = Chroma(
        persist_directory=persist_directory, 
        embedding_function=embeddings
    )

    # Verifique se há resultados relevantes
    results = db_excel.similarity_search_with_relevance_scores(query, k=1)
    if len(results) == 0 or results[0][1] < 0.7:
        # Retorna mensagem indicando que não foram encontradas fontes
        return "Não foram encontradas informações relevantes no banco de dados.", "Não foram encontradas fontes."

    # Criar uma cadeia de recuperação QA
    question_answering = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=db_excel.as_retriever(),
        memory=retaining_memory
    )

    # Mostra resposta
    answer = question_answering.invoke({"question": "Answer in brazilian portuguese and only with information that is in the documents provided." + query})
    result = answer['answer']

    # Mostra fonte utilizada para a resposta
    sources = []
    for doc, _score in results:
        metadata = ast.literal_eval(doc.page_content.split(" - ")[-1])  # Extrai o metadata
        sources.append(metadata.get("filename", "Fonte desconhecida"))  # Acessa o filename

    return result, sources
