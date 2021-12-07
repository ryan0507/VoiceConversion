# VoiceConversion
2021-2 YBIGTA Conference


#Preprocess Dataset

0. Install <b>ffmpeg</b> with apt and pip install <b>youtube-dl</b>
1. Set Playlist and get the URL of the youtube playlist
2. Get wav file below youtube-dl commands

```shell
youtube-dl --extract-audio --audio-format wav -i PLCVawrYUsJRvAIs5IxhbbksZtXFE0snnh 
```

--audio-format : Automatically executre ffmpeg <br>
-i : Identify playlist ID which placed after URL playlist=PLCVawrYUsJRvAIs5IxhbbksZtXFE0snnh


2. Use spleeter to seperate vocals and MR files (Can Skip)

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

For convenience already prepared at data_preprocessing.py

3. Change PATH if you need to change data_preprocessing.py
```python
if __name__ == '__main__':

    # Configuration of dataset path
    # CHANGE IF YOU NEED
    base_path = '/home/ryan0507/VoiceConversion/data/'
    dataset_dir = '/home/ryan0507/VoiceConversion/data'
```

4. After Run data_preprocessing.py you can get vocal and MR files for the playlist


