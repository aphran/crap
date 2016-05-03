#!/usr/bin/env python

import subprocess
import sys
from time import sleep

def filterwrite(line):
    if not "second" in line:
        #sys.stdout.write(line)
        print line,

process = subprocess.Popen(
    "cat pbuftext", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True
)

buf = ''
while True:
    out = process.stdout.read(1) #read 1 char
    if out:
        buf += out
        if out == '\n' or out == '\r':
            filterwrite(buf)
            sys.stdout.flush()
            buf = ''
    elif out == '' and process.poll() != None:
        break
    sleep(0.05)

