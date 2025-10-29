import ollama
import langchain_core
import langchain_ollama
import logging
from langchain_core.messages import ai

logging.getLogger("ollama")
logging.basicConfig(level=logging.INFO)

MODEL = "deepseek-r1:1.5b"

base_sys_prompt = [
    {"role": "system", "content": "You are a helpful assistant.Explain things in simple way."}
]

llm = langchain_ollama.ChatOllama(
    model=MODEL,
    temperature=0.8,   
)

def langchain_get_ai_answer(prompt: str,history:list) -> str | None:
    try:
        history.append({"role": "user", "content": prompt})
        response:ai.AIMessage= llm.invoke(input=history)


        # logging.info(response)
        return response.content
    except Exception as e:
        logging.error(e)
        return None

client = ollama.Client()
def get_ai_answer(prompt: str,history:list) -> str | None:
    try:
        response = client.chat(model=MODEL, 
                    messages=history + [{"role": "user", "content": prompt}])
        # logging.info(response)
        return response["message"]["content"]
    except Exception as e:
        logging.error(e)
        return None
    
def get_ai_info() -> dict | None:
    try:
        model_info = client.show(MODEL)
        logging.info(f"Model Info of {MODEL} Got.")
        return model_info
    except Exception as e:
        logging.error(e)
        return None
    

if __name__ == '__main__':
    print(langchain_get_ai_answer("What is deepseek?",base_sys_prompt))
