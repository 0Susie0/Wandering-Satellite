# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 14:49:25 2023

@author: XinyueHu
"""



NOTES_FLAT = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
NOTES_SHARP = ['C', '#C', 'D', '#D', 'E', 'F', '#F', 'G', '#G', 'A', '#A', 'B']

def NoteToMidi(KeyOctave):
    # KeyOctave is formatted like 'C#3'
    key = KeyOctave[:-1]  # eg C, Db
    octave = KeyOctave[-1]   # eg 3, 4
    answer = -1

    try:
        if 'b' in key:
            pos = NOTES_FLAT.index(key)
        else:
            pos = NOTES_SHARP.index(key)
    except:
        print('The key is not valid', key)
        return answer

    answer += pos + 12 * (int(octave) + 1) + 1
    return answer



def IOfile(fname, part):
    with open(fname + part[0], "r") as f1:
        with open(fname + part[1], "w") as f2:
            for line in f1:
                 note = line.strip('\n').split('-')
                 for x in note:
                     print(x)
                     f2.write(str(NoteToMidi(str(x))) + ';' + '\n')


filen = "D:\XinyueHu\ANU\COMP8350\Solo"
chords = ["\Chords.txt","\ChordsMiDi.txt"]
bass = ["\Bass.txt","\BassMiDi.txt"]
harmony = ["\Harmony.txt","\HarmonyMiDi.txt"]


