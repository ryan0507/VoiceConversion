import os
import librosa
import numpy as np
import soundfile as sf
from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter

def trim_audio_data(audio_file, save_file):
    sr = 16000
    start = 20
    end_sec = 30
    y, sr = librosa.load(audio_file, sr=sr)
    ny = y[sr* start:sr * end_sec]
    sf.write(save_file, ny, sr, format = 'WAV')

base_path = '/nfs/home/ryan0507/'
dataset_dir = '/nfs/home/ryan0507'
file_name = 'Dancing_Cartoon.wav'

separator = Separator('spleeter:2stems')
audio_loader = AudioAdapter.default()
sample_rate = 16000
trim_audio_data(base_path + file_name, base_path+'trim_'+file_name)
separator.separate_to_file(base_path+'trim_'+file_name, dataset_dir)

