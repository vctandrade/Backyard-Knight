# coding: cp437

import graphics
import screen
import pygame
import data

from operator import itemgetter

class SubmitScore (object):

    def __init__(self, score):
        data.playMusic("win-intro.ogg")

        self.menu_list = graphics.userInterface.Interface()

        self.menu_list.addButton(0, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.8,active=False)
        self.menu_list.addTextField(2, "textField2.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.6, color=0x000000, size=15)

        self.buff = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))
        
        self.transitionTimer = 0
        
        self.score = score
                        
    def displayOutput(self, display,offset=(0,0)):
        
        if self.transitionTimer <= 128:
            self.buff.fill((64 - self.transitionTimer / 2, 0,0))
            self.buff.set_alpha(self.transitionTimer * 3 + 1, pygame.RLEACCEL)
            graphics.drawText(self.buff, data.translate("name"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.5, size=int(30*self.transitionTimer*0.01) , color=0xFFFFFF, formatting="center")
        
        self.menu_list.draw(self.buff)

        graphics.drawText(self.buff, data.translate("submit"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.8, size=14 , formatting="center")
        
        display.blit(self.buff, (0, 0))
        self.transitionTimer += 1

    def respondToUserInput(self, event):
        for e in self.menu_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:

                pygame.mixer.music.fadeout(1024)

                transitionTimer = 0
                display = pygame.display.get_surface()
                static = display.copy()

                blackness = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))
                blackness.fill(0x000000)

                while transitionTimer <= 255:
                    display.blit(static, (0, 0))

                    blackness.set_alpha(transitionTimer, pygame.RLEACCEL)
                    display.blit(blackness, (0, 0))

                    transitionTimer += 1
                    pygame.display.flip()

                if e.button == 0:
                    ranking = data.load("ranking")
                    
                    ranking.append((self.menu_list.textFields[2].text, self.score))
                    ranking = sorted(ranking,key=itemgetter(1),reverse=True)

                    data.save(ranking,"ranking")
                    
                    return screen.Ranking()
            
        return self

    def update(self):
        
        if len(self.menu_list.textFields[2].text) >= 3:
            self.menu_list.buttons[0].active = True
        else:
            self.menu_list.buttons[0].active = False

