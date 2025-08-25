from dotenv import load_dotenv
import os 
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

def chat(prompt, temperature=0):
    llm = ChatOpenAI(
        openai_api_base="https://router.huggingface.co/v1",
        openai_api_key=os.environ["HF_TOKEN"],
        model_name="Qwen/Qwen3-Coder-480B-A35B-Instruct:fireworks-ai",
        temperature=temperature
    )

    prompt_template = PromptTemplate(
        input_variables=["question"],
        template="{question}"
    )

    chain = prompt_template | llm

    response = chain.invoke({"question": prompt})
    return response.content

if __name__ == "__main__":
    while True:
        prompt = input("enter query : ")
        print(chat(prompt, temperature=0.7))
