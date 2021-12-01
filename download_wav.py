from os import walk
from typing import Optional, List, Tuple
import os
import sys

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
    os.chdir(mypath)
    for f_link in link:
        os.system("youtube-dl --extract-audio " + f_link)
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
                cmdstr = "ffmpeg -i \"" + vidName + "\" -f wav -flags bitexact " + str(i) + ".wav"
                print(cmdstr)
                os.system(cmdstr)
                os.remove(vidName) #Will remove original opus file. Comment it if you want to keep that file.

if __name__ == '__main__':
    # ex : BOL4 나만봄
    # Add all of the list then it will transfer to all of the wav file
    # Use when implement dataset
    link = ['https://www.youtube.com/watch?v=AsXxuIdpkWM']
    path = "/direct/path/of/your/datafolder"
    download_youtube_wavfile(link,path)
