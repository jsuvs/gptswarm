## Voice wrapper around ChatGPT
Talk to ChatGPT down microphone and ChatGPT speaks back.

Uses OpenAI API to communicate with "chatgpt" and AWS Transcribe and Polly services for text to speech and vice-versa.

There's also an audio timeshifter feature, so you can tell ChatGPT to talk faster (say "speed up" or "slow down") and it'll speed up the audio playback.

One noticable problem is that if ChatGPT provides any sort of code in its answers then it speaks all the code out...

Requirements
- AWS account. Credentials set up with AWS CLI and with permissions to access AWS Polly and Transcribe services
- OpenAI API access. Set OPENAI_API_KEY environment variable
- A bunch of python libraries need to be imported
- python main.py

I'll tidy this up when I have time
