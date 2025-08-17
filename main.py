from pygame import *


win_width = 600
win_height = 500

window = display.set_model((win_width, win_height))
display.set_caption('ping pong mudah')

background_color = (0, 0, 0)
window.fill(background_color)

class GameSprite(sprite.Sprite):
  # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # We call the class constructor (Sprite):
        sprite.Sprite.__init__(self)
        # each sprite must store an image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

run = True
clock = time.Clock()
fps = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    
    window.fill(background_color)
    display.update()
    clock.tick(fps)
