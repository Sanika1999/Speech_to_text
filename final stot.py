# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:44:38 2020

@author: LENOVO
"""

from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
client = speech_v1.SpeechClient()
language_code = "en-US"
  # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
encoding = enums.RecognitionConfig.AudioEncoding.FLAC
config = {
        "audio_channel_count":2,#stereo to mono
        "language_code": language_code,
        "encoding": encoding,
    
    }
path='gs://speech_to_text123/Recording (4).flac'#choose your own path

audio = {"uri": path}

response = client.recognize(config, audio)
for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
