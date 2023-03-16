import os
from chatapi import ChatApi
from chatgpt import ChatGpt

#basic chat bot programmed to give short answers
apikey = os.getenv("OPENAI_API_KEY")
chatgpt = ChatGpt(ChatApi(apikey))
chatgpt.addSystemMessage("keep all responses to a very short length")
while True:
    message=input()
    print(chatgpt.send(message))
