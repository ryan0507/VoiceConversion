import numpy as np
import tensorflow as tf
import librosa
import os
import scipy.io.wavfile

def time_cutting(time, audio_path, save_path, resample):
  audio, sr = librosa.load(audio_path)
  real_audio = librosa.resample(audio, sr, resample)
  for i in range(int(len(real_audio) / (resample * time))):
    temp_audio = real_audio[resample * time * i:resample * time * (i + 1)]
    scipy.io.wavfile.write(save_path + 'splited' + str(i + 1) + '.wav', resample, temp_audio)

if __name__ == '__main__':
  time_cutting(4, 'NoMR_2.wav', 'flute_split/', 16000)