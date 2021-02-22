#Emmanuel Menier
#Lab 0: Helper methods to use in Lab 1

import os

nxt = 0
tail = 0

def myGetChar():
    global nxt
    global tail

    if nxt == tail:
        nxt = 0
        tail = read(0, 1024)

        if limit == 0:
            return None

    if next < (len(tail) - 1):
       char = chr(tail[nxt])
       nxt += 1
       return char
    else:
       return None

def myGetLine():
    global nxt
    global tail

    line = ""
    char = myGetChar()

    while(char != '' and char != None):
       line += char
       char = myGetChar()
    nxt = 0
    tail = 0
    return line

def myReadLine():
    lines = 0
    line  = myGetLine()

    while(len(line)):
       lines += 1
       line = myGetLine()
       
       
