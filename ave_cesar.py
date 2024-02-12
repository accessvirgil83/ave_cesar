import pyperclip
import sys


k = 13
mode = 1

if sys.argv[1]=="mode":
	mode=int(input("mode \n"))

msg = input("Press text \n")
SYMBOLS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'
SYM = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''
for i in msg:
    if i in SYM:
        stringIndex = SYM.find(i)
        if mode == 1:
            translatedIndex=stringIndex + k
        elif mode == 0:
            translatedIndex=stringIndex - k
        if translatedIndex >= len(SYM):
            translatedIndex=translatedIndex-len(SYM)
        elif translatedIndex<0:
            translatedIndex=translatedIndex+len(SYM)
        translated+=SYM[translatedIndex]
    else:
        translated+=i

print(translated)
pyperclip.copy(translated)
