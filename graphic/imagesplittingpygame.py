# import pygame

# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)

# pygame.init()


# class ImageDivider():
#     def __init__(self, file_name):
#         self.sprite_sheet = pygame.image.load(file_name).convert()

#     def get_image(self, x, y, width, height):
#         image = pygame.Surface([width, height]).convert()
#         image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
#         image.set_colorkey(BLACK)
#         return image

#     def get_images(self, oX, oY, lX, lY):
#         return [self.get_image(oX + lX * j, oY + lY * i, lX, lY)
#                 for i in range(4) for j in range(13)]


# size = (700, 500)
# screen = pygame.display.set_mode(size)

# originX = 0
# originY = 0
# lengthX = 56
# lengthY = 82

# deck = SpriteSheet("spanish-playing-cards-card-game-french-playing-cards-card.jpg")
# cards = deck.get_images(originX,originY,lengthX,lengthY)

# pygame.display.set_caption("My Game")

# done = False

# clock = pygame.time.Clock()
# i = 0
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

#     screen.blit(cards[i], [0, 0])
#     pygame.display.flip()
#     i = (i + 1) % 52
#     clock.tick(1)

# pygame.quit()
