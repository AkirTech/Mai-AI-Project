import os
import requests as req
import pygame.mixer as mixer
import time 
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def generate_reponse_au_name(content:str):
    return time.strftime(time.ctime()+content+".wav")


def play_audio(file_path):
    """Play an audio file using pygame mixer."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()

    # Wait for the audio to finish playing
    while mixer.music.get_busy():
        continue

def sget_audio(content:str,lang:str,ref_audio_path:str,
               prompt_text:str,prompt_lang:str,
               temperature:float = 1,top_k:int = 20):
    """Get an audio file from the api."""
    #     {
    #     "text": "",                   # str.(required) text to be synthesized
    #     "text_lang: "",               # str.(required) language of the text to be synthesized
    #     "ref_audio_path": "",         # str.(required) reference audio path
    #     "aux_ref_audio_paths": [],    # list.(optional) auxiliary reference audio paths for multi-speaker tone fusion
    #     "prompt_text": "",            # str.(optional) prompt text for the reference audio
    #     "prompt_lang": "",            # str.(required) language of the prompt text for the reference audio
    #     "top_k": 5,                   # int. top k sampling
    #     "top_p": 1,                   # float. top p sampling
    #     "temperature": 1,             # float. temperature for sampling
    #     "text_split_method": "cut0",  # str. text split method, see text_segmentation_method.py for details.
    #     "batch_size": 1,              # int. batch size for inference
    #     "batch_threshold": 0.75,      # float. threshold for batch splitting.
    #     "split_bucket: True,          # bool. whether to split the batch into multiple buckets.
    #     "speed_factor":1.0,           # float. control the speed of the synthesized audio.
    #     "streaming_mode": False,      # bool. whether to return a streaming response.
    #     "seed": -1,                   # int. random seed for reproducibility.
    #     "parallel_infer": True,       # bool. whether to use parallel inference.
    #     "repetition_penalty": 1.35    # float. repetition penalty for T2S model.
    #     "sample_steps": 32,           # int. number of sampling steps for VITS model V3.
    #     "super_sampling": False,       # bool. whether to use super-sampling for audio when using VITS model V3.
    # }
    po:dict = {"text": f"{content}",
        "text_lang": f"{lang}",
        "ref_audio_path": f"{ref_audio_path}",
        "prompt_text": f"{prompt_text}",
        "prompt_lang": f"{prompt_lang}",
        "top_k": top_k,
        "temperature": temperature, }
    response:req.Response = req.post("http://127.0.0.1:9980", json=po)
    logger.info(f"{response.status_code}")
    audio = response.content
    with open(f"{generate_reponse_au_name(content=content)}", "wb") as f:
        f.write(audio)
    return 0 if response.status_code == 200 else -1

def play_audio_file(file_path):
    """Play an audio file using the default system player."""
    os.system(f"start {file_path}")