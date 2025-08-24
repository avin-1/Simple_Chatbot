
from dotenv import load_dotenv
import os 
from openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(
    openai_api_base="https://router.huggingface.co/v1",
    openai_api_key=os.environ["HF_TOKEN"],
    model_name="Qwen/Qwen3-Coder-480B-A35B-Instruct:fireworks-ai",
    temperature=0
)
def chat(prompt):
    prompt_template=PromptTemplate(
        template=prompt
        )
    
    chain = prompt_template|llm         
    response=chain.invoke({})
    return response.content

if __name__=="__main__":
    while 1:
        prompt = input("enter query : ")
        print(chat(prompt))