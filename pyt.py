from pytube import *

import os

from moviepy.editor import *

name = str(input("What is the name you want to give to the file to download?"))

ext = str(input("What is the file extension? (mkv/mp4)"))

resolution = str(input("Resolution? (ex:720p)"))

ext = "." + ext

name = name + ext

url = str(input("url?"))

yt = YouTube(url)

yt.streams.filter(res='720p').first().download()

os.rename(yt.streams.filter(res=resolution).first().default_filename, name)

print("done :)")

extract = str(input("Do you want to extract the sound of the file? (y/n)"))

if extract == "y":

    ext = str(input("Extension of targeted audio file(mp3/wav)"))

    ext = "." + ext

    t = 0

    name2 = name

    name = " ".join(name)

    name = str.split(name) 

    ln = len(name) - 1

    while t < 4:

        name.pop(ln)

        ln = ln - 1

        t += 1 

    name = "".join(name)

    name = str(name)

    name = name + ext

    videoclip=VideoFileClip(name2)

    audioclip=videoclip.audio

    audioclip.write_audiofile(name)

    audioclip.close()

    videoclip.close()

    print("done :)")















