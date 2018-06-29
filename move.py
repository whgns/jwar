#!/usr/bin/python
from map import *

playerCoords = [1,1,0]

def pMove(x,y):
    global playerCoords
    playerCoords[0] += x
    playerCoords[1] += y
#    print playerCoords
    return playerCoords

def mInput(n):
    global urMap
    if str(n).lower() == "n": pMove(0,1)
    if str(n).lower() == "s": pMove(0,-1)
    if str(n).lower() == "e": pMove(1,0)
    if str(n).lower() == "w": pMove(-1,0)
    if str(n).lower() == "l": prLocal(playerCoords[0],playerCoords[1],playerCoords[2])
    if str(n) == "save": mapSave()
    if str(n) == "open": urMap = mapOpen()
    if str(n) == "generate": mapin()
    if str(n) == "map": print urMap
    if str(n).lower() == "q": quit()
    #else: print "Oh my no. mInput didn't work."

def pInfo(x,y,z):
    pPlace = getLocale(x,y,z)
    print pPlace[4]
#    print urMap

def mainloop():
    while True:
        mInput(raw_input("n/s/e/w: "))
        pInfo(playerCoords[0],playerCoords[1],playerCoords[2])

#print str(playerCoords)
#mInput("N")
#mInput("e")
mainloop()
