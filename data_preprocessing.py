from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter
from os import walk
from typing import Optional, List, Tuple
import os
import sys
import shutil
import subprocess

# Should be installed: youtube-dl , ffmpeg
'''
try:
        link = sys.argv[1]
except IndexError:
        scriptName = sys.argv[0]
        print("Usage: python " + scriptName + " linkOfVideo")
        exit()
'''

# mypath should be Absolute Path
def download_youtube_wavfile(link:List, mypath:str):
    if not os.path.exists(mypath):
        os.makedirs(mypath)
    os.chdir(mypath)
    for idx ,f_link in enumerate(link):
        p = subprocess.Popen("youtube-dl --rm-cache-dir", shell=True)
        p.wait()
        p = subprocess.Popen("youtube-dl --extract-audio " + f_link, shell=True)
        p.wait()
        vidID= f_link.split("=")[1]
        print("VidID = " + vidID)
        f = []
        for (dirpath, dirnames, filenames) in walk(mypath):
            f.extend(filenames)
            break
        print(f)
        for i in range(0, len(f)):
            if ".opus" in f[i] and vidID in f[i]:
                vidName = f[i]
                print(vidName)
                cmdstr = "ffmpeg -i \"" + vidName + "\" -f wav -flags bitexact " + str(idx) + ".wav"
                print(cmdstr)
                p = subprocess.Popen(cmdstr,shell=True)
                p.wait()
                os.remove(vidName) #Will remove original opus file. Comment it if you want to keep that file.

if __name__ == '__main__':
    # ex : BOL4 나만봄
    # Add all of the list then it will transfer to all of the wav file
    # Use when implement dataset
    #link = ['https://www.youtube.com/watch?v=AsXxuIdpkWM']
    link = []
    base_path = "/home/ryan0507/VoiceConversion/data"
    dataset_dir = '/home/ryan0507/VoiceConversion/data/'

    # READ text files
    f = open('/home/ryan0507/VoiceConversion/music_link.txt','r')
    line = f.readline().rstrip()
    while line:
        link.append(line)
        line = f.readline().rstrip()
    f.close()
    print(link)
    # Send Path youtube link and baes_path
    download_youtube_wavfile(link,base_path)

    separator = Separator('spleeter:2stems')
    audio_loader = AudioAdapter.default()
    sample_rate = 44100
    # waveform, _ = audio_loader.load('/home/ryan0507/VoiceConversion/data/0.wav')
    # prediction = separator.separate(waveform)
    for i in range(len(link)):
        separator.separate_to_file(base_path + '/' + str(i) + '.wav', dataset_dir)
