from chatapi import ChatApi

#wrapper around chatgpt ChatCompletion to act similar to chatgpt
class ChatGpt:
    def __init__(self, chat_api, logger=None):
        self.__api = chat_api
        self.__messages = []

    #send a message to chatgpt and return the response
    def send(self, message):
        self.addMessage("user", message)
        response = self.submit()
        return response.strip()
    
    #inserts system message
    def addSystemMessage(self, message):
        self.addMessage("system", message)

    #submit current conversation
    def submit(self):
        completion = self.__api.chat_completion_create(messages=self.__messages)
        self.__messages.append(completion.choices[0].message)
        latest_message_content=completion.choices[0].message.content
        return latest_message_content
    
    #add message to conversation
    def addMessage(self, role, content):
        msg = { 
            "role" : role,
            "content" : content
        }
        self.__messages.append(msg)