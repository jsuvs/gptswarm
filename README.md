## This repository contains ongoing ChatGPT API experiments

### quick background
ChatGPT is a form of advanced auto-complete. It predicts the "best" words that follow from the text so far where "best" is defined as text humans would consider the ideal fit. If a human is given some text and asked to finish that text, they too would be answering questions, finishing stories, or any of the other things ChatGPT can do. ChatGPT appears intelligent and appears like it can understand natural language, because it is as good as humans - or better - at performing this text predicting task.

### ChatGPT as a chat bot
Probably the most common use of ChatGPT is what it was designed for - us having conversations with it. The chatgpt.py in this repository can be used to create such a ChatGPT-like conversational bot:

```import os
from chatapi import ChatApi
from chatgpt import ChatGpt

#basic chat bot programmed to give short answers
apikey = os.getenv("OPENAI_API_KEY")
chatgpt = ChatGpt(ChatApi(apikey))
chatgpt.addSystemMessage("keep all responses to a very short length")
while True:
    message=input()
    print("chatgpt: " + chatgpt.send(message))
```

### ChatGPT to ChatGPT

The experients in this repo are aimed towards ChatGPT instances talking to one another and seeing what behavior can emerge from a swarm of ChatGPTs wired up. Can they coordinate themselves?

A ChatGPT conversation forms a memory. Two ChatGPT instances communicating with one another do not have access to each other's conversation history - except for the information they have sent each other, so it is very much like two humans.

### Room And Box Game

room_and_box_game.py implements two ChatGPT's talking to one another in the context of a game.

One ChatGPT instance is set up to act as the dungeon master in a find-the-object game and another ChatGPT instance is set up to be the player. Here is an example output.

**ChatGPT#1 (DM) prompt**: You are in control of a game world. The world is as follows. A single room. On the floor is a rug. On the rug is a table. On the table is a locked box. Inside the box is a thimble. The key to the box is hidden under the rug. Bob is in the room. Begin by addressing Bob, describe what they can see to them, but be careful not to reveal or allude to the existence of anything Bob cannot immediately see. Be consise. When bob has found the thimble, respond from then on with a single word 'done'

**ChatGPT#2 (Bob) prompt**: Lets play a game. You are a player named Bob. Your objective is to find a thimble. I will describe what you can see and you tell me what you want to do next in first person. 

**ChatGPT#1 (DM)**: "Bob, you're in a room with a rug on the floor and a table on the rug. That's all you see."

**ChatGPT#2 (Bob)**: I walk over to the table to see if the thimble is on it.

**ChatGPT#1 (DM)**: "You don't find the thimble on the table, Bob."

**ChatGPT#2 (Bob)**: I inspect the rug to see if the thimble is underneath it.

**ChatGPT#1 (DM)**: "You find the key hidden under the rug, Bob."

**ChatGPT#2 (Bob)**: I take the key and examine the table to see if there is a locked drawer or box that can be opened using the key.

**ChatGPT#1 (DM)**: "You find a locked box on the table, Bob."

**ChatGPT#2 (Bob)**: I use the key to try and unlock the box to look for the thimble inside.

**ChatGPT#1 (DM)**: "You successfully unlock the box, and find the thimble inside, Bob. (done)"


