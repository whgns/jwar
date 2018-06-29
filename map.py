#!/usr/bin/python

import pickle
from random import randint
urMap = []
Locations = ["A dusty rest stop.","A grassy knoll.","A rocky outcropping","At the foot of a mountain, a visa.","A road wanders here."]


def getmap():
    rootsize = int(raw_input("How big is the square map?"))
    return rootsize

def mapin():
    mLen = getmap()
    mapX = mLen
    mapY = mLen
    z = 0 

    for x in range(0,mapX):
#        print "X: "+ str(x)
        urMap.insert(x, [])
#        print str(urMap[x])
        for y in range(mapY):
            urMap[x].insert(y, [])
            # datastructure is [x/y/z coordinates {0-2}, Area, Description]
            
            initData = [x, y, z, 0, Locations[randint(0,4)]]
            urMap[x][y].append(initData)    
#    print urMap
#    return "doneZo"

def getLocale(x,y,z):
    mapticle = urMap[x][y][z]
    return mapticle

def prLocal(x,y,z):
    print "urMap[x] = ", urMap[x]
    print "urMapXY = ", urMap[x][y]
    mipMop = urMap[x][y][z][4]
    print mipMop

def mapSave():
    print "writing map file"
    global urMap
    yrMap = open("urMap.jw", "w+b")
    pickle.dump(urMap, yrMap)

def mapOpen():
    global urMap
#    print "yoyo:", str(urMap)
    print "opening map file"
    yrMap = open("urMap.jw", "r")
    print "reading map file"
    urMap = pickle.load(yrMap)
#    print urMap
    print "whatever. i tried"
    return urMap

#mapin()
#print getLocale(0,0,0)

