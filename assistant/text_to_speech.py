import numpy as np
import boto3

#Wrapper around AWS text to speech service
class TextToSpeech:
    def __init__(self, sample_rate):
        self.__client = boto3.client('polly')
        self.__sample_rate = sample_rate

    def to_speech(self, text):
        response = self.__client.synthesize_speech(
            Engine='neural',
            LanguageCode='en-GB',
            OutputFormat='pcm',
            SampleRate=str(self.__sample_rate),
            Text=text,
            TextType='text',
            VoiceId='Amy'
        )
        audio = response['AudioStream'].read()
        int16_array = np.frombuffer(bytes(audio), dtype = np.int16)
        return int16_array
