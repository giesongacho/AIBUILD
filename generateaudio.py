from selenium import webdriver
from splinter import browser
import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/g5CIjZEefAph4nQFvHAz"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "983efdf07e9267a3378352228051d5ca"
}

url = browser.url
response = requests.get(url)
tts = response.request.params['text']

data = {
  "text": tts,
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

def translate_english(event):
requests.post(url, json=data, headers=headers)
with open('ttsmenaudio.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)