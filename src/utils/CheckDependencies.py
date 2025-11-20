import subprocess as sp
import os
import logging
logger = logging.getLogger("CheckDependencies")
logger.setLevel(logging.INFO)
logger.info("Checking Dependencies.")
logger.addHandler(logging.StreamHandler())

def check_ollama_installed() -> bool:
    try:
        result = sp.run(["ollama", "--version"], capture_output=True, text=True)
        # logger.info(f"{result.stdout}")
        if "client version" in result.stdout.lower() or "ollama version" in result.stdout.lower():
            logger.info("Ollama is installed.")
            return True
        else:
            logger.error("Ollama is not installed. Please install Ollama from https://ollama.com/")
            return False
    except FileNotFoundError:
        return False
    
def redierct_ollama_models(path:str):
    try:
        os.system(f"setx OLLAMA_MODELS {path}\\models")
        logger.info("Ollama models redirected to %s" % path)
        logger.info("Restarting ollama")
        os.system("taskkill /f /im ollama.exe")
        os.system("ollama serve")
        logger.info("Ollama restarted")
    except Exception as e:
        logger.error(e)


def check_gs_installed() -> bool:
    ...
    
if __name__ == '__main__':
    # if not logger.hasHandlers():
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #     logger.addHandler(logging.StreamHandler())

    if check_ollama_installed():
        logger.info("Ollama is installed.")
        os.system("./scripts\\start_ollama.bat")
        
    else:
        logger.error("Ollama is not installed. Please install Ollama from https://ollama.com/")