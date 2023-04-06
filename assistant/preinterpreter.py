
import asyncio

#monitors the transcribed text as the user speaks
#determines whether the user has finished speaking
#also recognizes a few commands which are currently hardcoded
class PreInterpreter:
    def __init__(self, transcriber, query_handler, speaker):
        self.__accumulated_text = ""
        self.__transcriber = transcriber
        self.__query_handler = query_handler
        self.__timer = None
        self.__speaker = speaker

    #called when the user has finished their query
    def __on_query_end_timer(self):
        #print("timer fire")
        #issue the user query to the handler
        self.__query_handler.send_message(self.__accumulated_text)
        self.__accumulated_text=""

    #begin preinterpreter
    #speaking_pause_secs    time in seconds of silence interpreted as end of speaking
    async def go(self, speaking_pause_secs):
        while True:
            (text, is_complete) = await self.__transcriber.get_transcript()
            #print(text)
            if is_complete:
                print("[complete] " + text)
                command = text.lower().replace('.','')
                if command == "cancel that":
                    self.__accumulated_text = ""
                    continue
                if command == "speed up":
                    self.__speaker.speed *= 1.2
                    continue
                if command == "slow down":
                    self.__speaker.speed *= 0.8
                    continue
                self.__accumulated_text += text
            #else:
            #   print("[partial] " + text)

            #reset timer used to detect speaking pause
            if self.__timer != None:
                self.__timer.cancel()
            loop = asyncio.get_event_loop()
            self.__timer = loop.call_later(speaking_pause_secs, self.__on_query_end_timer)
