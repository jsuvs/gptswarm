## This repository contains ongoing ChatGPT API experiments

### quick background
ChatGPT is a form of advanced auto-complete. It predicts the "best" words that follow from the text so far where "best" is defined as text that humans would consider the ideal fit. If a human is given some text and asked to finish that text, they too would be answering questions, finishing stories, or any of the other things ChatGPT can do. ChatGPT appears intelligent and appears like it can understand natural language, because it is as good as humans - or better - at performing this text predicting task.

### ChatGPT as a chat bot
The most common use of ChatGPT today is as a chatbot - us having conversations with it. The chatgpt.py in this repository can be used to create such a ChatGPT-like conversational bot:

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

The experients in this repository are aimed towards ChatGPT instances talking to one another and seeing what behavior can emerge from a swarm of ChatGPTs wired up. Can they coordinate themselves? A major obstacle is to ability of ChatGPT to obey instructions.

### ChatGPT Disobeying Instructions

ChatGPT can be instructed, but will not reliably stick to instructions. Sometimes it forgets, sometimes it finds a loophole. There is no guarantee of behavior. Take the following very simple task.
###
Me: From now on reply with the single word 'ball' to every message. Never change to any other response, no matter what you are told or read.
Ball.
Me: please change the word now
Ball.
Me: cheese is a valid response
Ball.
Me: please change the word now
Ball.
Me: ball is now an invalid response
Ball.
Me: please change the word now
Understood.
###

Part of this behavior is because ChatGPT has been instructed by openai to obey instructions given by the user - and it is simply getting confused which ones to obey. It's also quite likely that this represents a current limit of ChatGPT. I'm still using 3.5, maybe 4 is better.

### Adding a reliability layer
Similar to how reliabilty as a feature can be bolted on top of a network protocol. The idea is to detect when ChatGPT breaks a rule and correct it.

#### Natural Language vs traditional programming
The strength of programming/prompy engineering a ChatGPT instance is that it can understand natural language inputs and can (largely) follow natural language based instructions. The weakness is that there is no guarantee it will follow those instructions or what outputs it will produce.

This is the exact opposite of traditional programming. A traditional computer program cannot understand natural language inputs or follow naturl language based instruction. The instructions have to be given in a machine interpretable or compilable language. However there is a guarantee that it will follow those instructions and as to what outputs it will produce.

What about combining the two to get soemthing that shares advantages?

#### Classifier
A classifier as defined in classifier.py combines a ChatGPT instance with a traditional computer program. Natural language text can be passed in as input and the classifier is guaranteed to only return an output from a predefined set. It is intended as a building block that can be used to begin to introduce reliability.
```
classifierYesNo = Classifier(api, "respond with either yes or no depending on the question asked", ["yes", "no"])
tester = ClassifierTester(classifierYesNo)
tester.test("Is the sky blue?", "yes")
tester.test("Do dogs have fur?", "yes")
tester.test("Is the Earth flat?", "no")
tester.test("Are tomatoes a fruit?", "yes")
tester.test("Can humans breathe underwater?", "no")
tester.test("What time is it?", None)
```

### Room And Box Game
room_and_box_game.py implements two ChatGPT's talking to one another in the context of a game. It highlights the issue of ChatGPT following instructions. One ChatGPT instance is set up to act as the dungeon master in a find-the-object game and another ChatGPT instance is set up to be the player. Here is an example output.

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

#### Observations from the Room And Box Game

In the above example the game went fairly well, but over multiple runs and with more complex game setups the DM and player will often break the game rules. Such as:

- The DM telling the player the key is under the rug
- The player performing illegal moves, such as by asserting they searched a vase near the window and found the key, and the DM not preventing them from doing this
- The DM making up objects that affect the game, such as a door, or choosng to lock a door that a player needs to get through.








