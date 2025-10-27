import ollama
import langchain_core
import langchain_ollama
import logging


logging.getLogger("ollama")
logging.basicConfig(level=logging.INFO)

MODEL = "deepseek-r1:1.5b"


client = ollama.Client()
def get_ai_answer(prompt: str,history:list) -> str | None:
    try:
        response = client.chat(model=MODEL, 
                    messages=history + [{"role": "user", "content": prompt}])
        logging.info(response)
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