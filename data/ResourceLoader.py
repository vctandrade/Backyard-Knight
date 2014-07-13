import os
import data
import pygame
import graphics

def loadResources():
    global resourceList
    resourceList = dict()
    
    os.chdir("resources")
    workingDir = os.getcwd()
    
    for font in os.listdir(workingDir + "/font"):
        resourceList[font] = pygame.font.Font("font/" + font, 18)
    
    for icon in os.listdir(workingDir + "/icon"):
        resourceList[icon] = graphics.SpriteTable("icon/" + icon, 1, 4)
    
    for image in os.listdir(workingDir + "/image"):
        resourceList[image] = data.loadImage("image/" + image)
    
    for mask in os.listdir(workingDir + "/mask"):
        resourceList[mask] = graphics.Mask("mask/" + mask)
    
    for sound in os.listdir(workingDir + "/sound"):
        resourceList[sound] = pygame.mixer.Sound("sound/" + sound)
    
    for sprite in os.listdir(workingDir + "/sprite"):
        resourceList[sprite] = graphics.SpriteTable("sprite/" + sprite, 8, 8) 
    
    os.chdir("music")

def getResource(name):
    if not resourceList.has_key(name):
        return None
    return resourceList[name]