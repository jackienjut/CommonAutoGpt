from dotenv import load_dotenv, find_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

_ = load_dotenv(find_dotenv())

prompt =PromptTemplate.from_template("你是一个起名大师，帮我起一个具有{county}特色的男孩名字")

llm = ChatOpenAI(temperature=0,model = "gpt-3.5-turbo")

response = llm.invoke(prompt.format(county = "中国"))
print(response.content)
