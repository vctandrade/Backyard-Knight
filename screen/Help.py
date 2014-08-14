import graphics
import screen
import data


class Help(object):

    def __init__(self):
        self.help_list = graphics.userInterface.Interface()
        self.help_images = ["help_image1.png", "help_image2.png", "help_image3.png"]

        self.image = 0
        button_width = data.getResource("button.png").width
        button_height = data.getResource("button.png").height

        self.help_list.addButton(0, "button.png", data.config.WIDTH * 0.1 - (button_width) / 2 , data.config.HEIGHT * 0.1 - (button_height) / 2)
        self.help_list.addButton(1, "button.png", data.config.WIDTH * 0.4 - (button_width) / 2 , data.config.HEIGHT * 0.9 - (button_height) / 2)
        self.help_list.addButton(2, "button.png", data.config.WIDTH * 0.6 - (button_width) / 2 , data.config.HEIGHT * 0.9 - (button_height) / 2)

    def displayOutput(self, display):
        self.help_list.draw(display)
        display.blit(data.getResource(self.help_images[self.image]), (400, 200))

    def respondToUserInput(self, event):
        for e in self.help_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                    if e.button == 0:
                        return screen.Menu()
                    if e.button == 1 :
                        self.image -= 1
                    if e.button == 2:
                        self.image += 1

                    self.image %= 3

        return self

    def update(self):
        pass
