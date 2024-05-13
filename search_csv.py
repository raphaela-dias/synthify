from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
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

agent_executer = create_csv_agent(llm, 'test\Base Chamados_V1.xlsx - Base .csv', verbose = False)

answer = agent_executer.invoke("Quantos tickets resolvidos existe no arquivo?")

print(answer['output'])