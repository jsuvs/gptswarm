## This repository contains ongoing ChatGPT API experiments

In particular what emerges when multiple ChatGPT instances are wired up to talk to each other in different roles?

For example see the following output from room_and_box_game.py which sets up one ChatGPT instance to act as the DM in a find-the-object game and another ChatGPT instance to play it.

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

### Observations

The prompts above need improvement as
- The DM ChatGPT often suggests looking under the rug - I guess that technically isn't breaking the rules
- The player can enter storytelling mode explaining that it searched a vase near the window and found the key, the DM then believes it has


