#!/usr/bin/env python
# coding=utf-8

import os
import sys

from pydub import AudioSegment as AS

def convert(filename, savename, oformat):
    """
    filename: file you want to convert
    savename: file you want to save
    oformat:  file format you want to save as
    """
    afset = ["wav", "mp3", "mp4", "ogg", "flv", "raw", "m4a"]
    
    splitstr = os.path.splitext(filename)[-1][1:]
    if splitstr not in afset or oformat not in afset:
        print("Wrong file format, exit!")
        sys.exit()
    else:
        audio = switcher(filename)
        audio.export(savename, format=oformat)
        print("File converted!")

def switcher(filename):
    splitstr = os.path.splitext(filename)[-1][1:]
    if splitstr == "wav":
        audio = AS.from_wav(filename)
        return audio
    elif splitstr == "mp3":
        audio = AS.from_mp3(filename)
        return audio
    elif splitstr == "ogg":
        audio = AS.from_ogg(filename)
        return audio
    elif splitstr == "flv":
        audio = AS.from_flv(filename)
        return audio
    elif splitstr == "raw":
        audio = AS.from_raw(filename)
        return audio
    else:
        audio = AS.from_file(filename)
        return audio

convert("planet.mp4", "planet.mp3", "mp3")
# cannot convert mp4 to m4a, wav, flv, ogg, raw
# we'll fix this issue later
#convert("planet.mp4", "planet.m4a", "m4a")
#convert("planet.mp4", "planet.wav", "wav")
#convert("planet.mp4", "planet.flv", "flv")
#convert("planet.mp4", "planet.ogg", "ogg")
#convert("planet.mp4", "planet.raw", "raw")
