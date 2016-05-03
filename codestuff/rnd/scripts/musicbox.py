#!/usr/bin/env python3
import subprocess

# freqs
freqs = {
'C' : 261.6,
'C#': 277.2,
'D' : 293.7,
'D#': 311.1,
'E' : 329.6,
'F' : 349.2,
'F#': 370.0,
'G' : 392.0,
'G#': 415.3,
'A' : 440.0,
'A#': 466.2,
'B' : 493.9,
'C1': 523.2,
}

song_name = "I love you, and you love me"
song_author = "Barney and friends"
song_src = " \
g g  g g  e e  g g  \
g g  g g  e e  g g  g g \
a a  g g  f f  e e  \
d d  e e  f f  f f  \
e e  f f  g g  c c  c c \
c d  d e  e f  f g  \
g g  d d  d d  f f  \
e e  d d  c c  c c  \
"

length = 125
song_frq = [freqs[note] for note in song_src.upper().split()]
song_args = []
for note in song_frq:
    song_args.append("-n")
    song_args.append("-l {0}".format(str(length)))
    song_args.append("-f {0}".format(str(note)))
song_args[0] = "beep"
print("Playing \"{0}\" by \"{1}\"".format(song_name, song_author))
#print("calling <<{0}>>".format(" ".join(song_args)))
try:
    subprocess.call(song_args)
except:
    print("Error calling 'beep' command")
    raise
