import openai
import time

#wrapper around openai api, mainly to provide retry in the face of the rate limit
class ChatApi:
    def __init__(self, apikey, logger=None):
        openai.api_key = apikey
        self.__retry_interval_min = 10
        self.__retry_interval_max = 90
        self.__retry_interval = 5
   
    #call chat completion api, retry on failure
    def chat_completion_create(self, messages, temperature=0.8):
        while True:
            try:
                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=temperature)
                #get slowly faster
                self.__retry_interval = max(self.__retry_interval - 1, self.__retry_interval_min)
                break
            except AttributeError as exc:
                #TODO this might not be a rate limit error, it might be some other error
                print(exc)
                time.sleep(self.__retry_interval_secs)
                #slow down
                self.__retry_interval = min(self.__retry_interval * 2, self.__retry_interval_max)
                continue
        return completion
