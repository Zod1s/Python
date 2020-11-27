import pygame
import GraphicEngineV2 as g

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
size = (600,600)

done = False

g.screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

cube = g.Cube([300, 300, 0], 10)
itemlist = [cube]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    for key in g.key_to_func:
        if pygame.key.get_pressed()[key]:
            g.key_input(key, itemlist)

    g.screen.fill(BLACK)

    for item in itemlist:
        item.show()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()