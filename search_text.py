from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import os

# Loading api key
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

# Defining the model
llm = ChatOpenAI(
    openai_api_key= api_key,
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

# Loading all documents from a directory into a list
directory_path = "./test"
documents = []

# Loop through all files and subdirectories in the main directory
for root, dirs, files in os.walk(directory_path):

    for filename in files:

        file_path = os.path.join(root, filename)
        # Identify and load document based on extension
        if filename.endswith(".pdf"):
            pdf_loader = PyPDFLoader(file_path)
            print(filename)
            document = pdf_loader.load()
        elif filename.endswith((".txt", ".doc", ".docx")):
            text_loader = TextLoader(file_path)
            print(filename)
            document = text_loader.load()

        # Split the current document
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,  
            chunk_overlap=70
        )

        split_docs = text_splitter.split_documents(document)

        # Add the split chunks
        documents.extend(split_docs)

# Embedding the chunks to vectorstores
embeddings = OpenAIEmbeddings(openai_api_key=api_key)
persist_directory = 'db'

# Creating vector database
my_database = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=persist_directory
)

# Defining the conversational memory
retaining_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

# Defining the retriever
question_answering = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=my_database.as_retriever(),
    memory=retaining_memory
)

# Conversation with the AI
question = input("Insira sua pergunta: ")
result = question_answering.invoke({"question": "Answer in brazilian portuguese and only with information that is in the documents provided." + question})
print(result['answer'])

# Show sources used for the answer
results = my_database.similarity_search_with_relevance_scores(question, k=1)
if len(results) == 0 or results[0][1] < 0.7:
    print(f"Unable to find matching results.")
else:
    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Sources: {sources}"
    print(formatted_response)