import queue
import os
from text_to_speech import TextToSpeech
import sys
sys.path.append("..")
from chatgpt import ChatGpt
from chatapi import ChatApi

class QueryHandler:
    def __init__(self, play_queue):
        self.__queue = queue.Queue()
        self.__text_to_speech = TextToSpeech(16000)
        apikey = os.getenv("OPENAI_API_KEY")
        self.__chatgpt = ChatGpt(ChatApi(apikey))
        self.__play_queue = play_queue
        
    def send_message(self, text):
        self.__queue.put_nowait(text)

    def run(self):
        while True:
            message = self.__queue.get()
            print("[to gpt] " + message)
            response = self.__chatgpt.send(message)
            print("[gpt response]: " + response)
            audio_bytes=self.__text_to_speech.to_speech(response)
            audio_bytes = audio_bytes.reshape((audio_bytes.shape[0], 1))
            self.__play_queue.put_nowait(audio_bytes)

