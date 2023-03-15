import openai

#wrapper around chatgpt ChatCompletion to act similar to chatgpt
class ChatGpt:
    def __init__(self, apikey, logger=None):
        openai.api_key = apikey
        self.__messages = []

    def send(self, message):
        self.addMessage("user", message)
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.__messages)
        self.__messages.append(completion.choices[0].message)
        latest_message_content=completion.choices[0].message.content
        return latest_message_content
    
    def addSystemMessage(self, message):
        self.addMessage("system", message)

    def addMessage(self, role, content):
        msg = { 
            "role" : role,
            "content" : content
        }
        self.__messages.append(msg)