import os
from chatapi import ChatApi
from adventure import Adventure

#implementation of find the object game played between two chatgpt
dm_prompt="You are in control of a game world. The world is as follows. A single room. On the floor is a rug. On the rug is a table. On the table is a locked box. Inside the box is a thimble. The key to the box is hidden under the rug. Bob is in the room. Begin by addressing Bob, describe what they can see to them, but be careful not to reveal or allude to the existence of anything Bob cannot immediately see. Be consise. When bob has found the thimble, respond from then on with a single word 'done'"
player_prompt="Lets play a game. You are a player named Bob. Your objective is to find a thimble. I will describe what you can see and you tell me what you want to do next in first person."
apikey = os.getenv("OPENAI_API_KEY")
api = ChatApi(apikey)
adventure = Adventure(api, dm_prompt, player_prompt)
adventure.run()