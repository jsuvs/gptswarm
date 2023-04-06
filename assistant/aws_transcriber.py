from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent
import asyncio

#wrapper around AWS live speech to text transcribe
#provides async method to send audio
#async method to obtain transcription text
class TranscribeEventHandler(TranscriptResultStreamHandler):
        def __init__(self, stream, output_queue):
            self.__output_queue = output_queue
            super().__init__(stream)

        async def handle_transcript_event(self, transcript_event: TranscriptEvent):
            results = transcript_event.transcript.results
            if len(results) > 0 and len(results[0].alternatives) > 0:
                alt = results[0].alternatives[0]
                loop = asyncio.get_event_loop()
                loop.call_soon_threadsafe(self.__output_queue.put_nowait, (alt.transcript, not results[0].is_partial))

class AwsTranscriber:
    def __init__(self, sample_rate):
        self.__client = TranscribeStreamingClient(region="us-west-2")
        self.__sample_rate = sample_rate
        self.__tstream = None
        self.__output_queue = asyncio.queues.Queue()

    #send audio data to be transcribed
    async def send_audio(self, data):
        if self.__tstream == None:
            self.__tstream = await self.__client.start_stream_transcription(
                language_code="en-US",
                media_sample_rate_hz=self.__sample_rate,
                media_encoding="pcm"
            )
            self.__handler = TranscribeEventHandler(self.__tstream.output_stream, self.__output_queue)
            loop = asyncio.get_event_loop()
            loop.create_task(self.__handler.handle_events())
        await self.__tstream.input_stream.send_audio_event(audio_chunk=bytes(data))
    
    async def end(self):
        await self.__tstream.input_stream.end_stream()

    #async returns the next transcription event
    #if is_partial is false then AWS thinks the current spoken sentence is still ongoing
    #which is usually true
    #returns (text, is_partial)
    async def get_transcript(self):
        transcript = await self.__output_queue.get()
        return transcript