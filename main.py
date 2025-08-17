from pygame import *


win_width = 600
win_height = 500

window = display.set_model((win_width, win_height))
display.set_caption('ping pong mudah')

background_color = (0, 0, 0)
window.fill(background_color)

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
