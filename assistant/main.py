#chatgpt based voice assistant
#uses AWS for voice to text and text to voice
#requires:
#-connected microphone and speaker
#-AWS credentials configured (using AWS CLI)
#-AWS permissions to access Transcribe and Polly services
#-OpenAI API access (set OPENAI_API_KEY environment variable)
import asyncio
import threading
import sys
from audiolib import Microphone, Speaker
from aws_transcriber import AwsTranscriber
from query_handler import QueryHandler
from preinterpreter import PreInterpreter

play_queue = asyncio.Queue()
#sends queued audio data to speaker
async def post_speaker(speaker : Speaker):
    while True:
        audio_bytes = await play_queue.get()
        speaker.stop()
        speaker.play(audio_bytes)

#funnels microphone output to transcriber
async def mic_to_transcriber(microphone : Microphone, transcriber : AwsTranscriber):
    async for data in microphone.get_data():
        await transcriber.send_audio(data)
    await transcriber.end()

async def main():
    print("begin")
    sample_rate=16000
    block_size=2048
    microphone = Microphone(sample_rate, block_size)
    speaker = Speaker(sample_rate, block_size)
    transcriber = AwsTranscriber(sample_rate)
    loop = asyncio.get_event_loop()
    #begin query handler that will accept queries to send to chatgpt
    #for now this is blocking so runs on seperate thread
    query_handler = QueryHandler(play_queue)
    thread = threading.Thread(target=query_handler.run)
    thread.start()
    #start the chain from microphone to speaker
    preinterpreter = PreInterpreter(transcriber, query_handler, speaker)
    await asyncio.gather(
        mic_to_transcriber(microphone, transcriber),
        preinterpreter.go(2),
        post_speaker(speaker)
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()