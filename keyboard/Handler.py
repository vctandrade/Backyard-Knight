import pygame
import collections

delay = 20
period = 4

ticks = 0
lastUni = None

multiKeys = collections.OrderedDict()

def setMultiKeys(*keys):
    multiKeys.clear()
    for i in keys: multiKeys[i] = None

def handle(event):
    global lastUni, ticks

    if event.type == pygame.KEYDOWN:
        if event.key in multiKeys:
            multiKeys[event.key] = event

        else: lastUni = event; ticks = 0

    if event.type == pygame.KEYUP:
        if event.key in multiKeys:
            multiKeys[event.key] = None

        else: lastUni = None; ticks = 0

def tick():
    global ticks
    if lastUni: ticks += 1

def getPressed():
    eventList = list()

    for i in  multiKeys.values():
        if i: eventList.append(i)

    if (lastUni == None or ticks != 0) \
        and (ticks < delay or ticks % period > 0): pass
    else: eventList.append(lastUni)

    return eventList
