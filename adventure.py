from chatgpt import ChatGpt

#implementation of an adventure game played between one chatgpt in the role of the dungeon master and another chatgpt in the role of the player
#the provided dm_prompt should specify the game rules and the player_prompt the rules for the player
#the game terminates when the dm says "done" or when a maximum number of rounds is reached
class Adventure:
    def __init__(self, chatapi, dm_prompt, player_prompt, max_rounds=50, logger=None):
        self.__api = chatapi
        self.__dm_prompt = dm_prompt
        self.__player_prompt = player_prompt
        self.__maxrounds = max_rounds

    #run the game
    def run(self):
        dm_prompt = self.__dm_prompt
        player_prompt = self.__player_prompt
        print("dm prompt: {}\n".format(dm_prompt))
        print("bob (player) prompt: {}\n".format(player_prompt))
        dm = ChatGpt(self.__api)
        dm.addSystemMessage("keep all responses to a very short length")
        #set up the DM with the game setup prompt
        dm_response = dm.send(dm_prompt)
        self.print_dm_response(dm_response)
        player = ChatGpt(self.__api)
        #set up the player with their rules prompt followed by an intro by the DM
        player_response = player.send(player_prompt + "\n" + dm_response)
        self.print_player_response(player_response)
        for i in range(self.__maxrounds):
            dm_response = dm.send("bob: {}".format(player_response))
            self.print_dm_response(dm_response)
            #try to detect the single "done" message from the DM which terminates the game. List of some formats I've seen:
            #Done.
            #"done"
            #(done)
            if len(dm_response) < 8 and "done" in dm_response.lower():
                break
            player_response = player.send(dm_response)
            self.print_player_response(player_response)

    def print_dm_response(self, response):
        print("dm: {}\n".format(response))
    def print_player_response(self, response):
        print("bob: {}\n".format(response))
