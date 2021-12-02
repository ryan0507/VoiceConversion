# VoiceConversion
2021-2 YBIGTA Conference


#Preprocess Dataset

0. Install <b>ffmpeg</b> with apt and pip install <b>youtube-dl</b>
1. Use download_wav.py

```python
if __name__ == '__main__':
    # ex : BOL4 나만봄
    # Add all of the list then it will transfer to all of the wav file
    # Use when implement dataset
    link = ['https://www.youtube.com/watch?v=AsXxuIdpkWM']
    path = "/direct/path/of/your/datafolder"
    download_youtube_wavfile(link,path)
```

Change link list to prepare raw .wav files

2. Use spleeter to seperate vocals and MR files

You can find <b>Separator</b> class with <b>spleeter.separator</b>
```python
from spleeter.separator import Separator

# Using embedded configuration.
separator = Separator('spleeter:2stems')

# Using custom configuration file.
separator = Separator('/path/to/config.json')

```

You can find AudioAdapter to sperate files <b>spleeter.audio.adapter</b>


```python
# Use audio loader explicitly for loading audio waveform :
from spleeter.audio.adapter import AudioAdapter

audio_loader = AudioAdapter.default()
sample_rate = 44100
waveform, _ = audio_loader.load('/path/to/audio/file', sample_rate=sample_rate)

# Perform the separation :
prediction = separator.separate(waveform)
```
https://github.com/deezer/spleeter/wiki/4.-API-Reference#separator