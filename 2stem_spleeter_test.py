from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter

separator = Separator('spleeter:2stems')
audio_loader = AudioAdapter.default()
sample_rate = 44100
waveform, _ = audio_loader.load('/home/ryan0507/VoiceConversion/data/0.wav')
prediction = separator.separate(waveform)

separator.separate_to_file('/home/ryan0507/VoiceConversion/data/0.wav','/home/ryan0507/VoiceConversion/data/' )