from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter
from os import walk
from typing import Optional, List, Tuple
import os
import sys
import shutil
import subprocess
import glob

if __name__ == '__main__':

    # Configuration of dataset path
    # CHANGE IF YOU NEED
    base_path = '/home/ryan0507/VoiceConversion/data/'
    dataset_dir = '/home/ryan0507/VoiceConversion/data'


    pattern = base_path + '*wav*'
    result = glob.glob(pattern)
    print(result)

    for idx, file_name in enumerate(result):
        old_name = file_name
        new_name = base_path + str(idx) + '.wav'
        os.rename(old_name, new_name)

    new_result = glob.glob(pattern)
    print(new_result)

    # Seperate vocal and MR with spleeter
    # You should use TF <= 2.5.0
    separator = Separator('spleeter:2stems')
    audio_loader = AudioAdapter.default()
    sample_rate = 44100
    # waveform, _ = audio_loader.load('/home/ryan0507/VoiceConversion/data/0.wav')
    # prediction = separator.separate(waveform)
    for file_name in new_result:
        separator.separate_to_file(file_name, dataset_dir)
