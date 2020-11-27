import pygame
import math
from tkinter import Tk, Button

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
mod   = (  3,   5,  10)

white_pos = [  0, 0]
black_pos = [290, 0]

HEIGHT = 18
WIDTH = 40

mode = 0
x = 0
y = 1

class Player():
    def __init__(self):
        self.time = 0
        self.time_coordinates = []  
        self.colour = ""    
        self.background_colour  = ""
        self.sign_colour = ""

    def timer(self):
        if self.time >  0.01:
            pygame.time.delay(10)
            self.time -= 0.01

        minutes = math.floor(self.time // 60)
        seconds = math.floor(self.time % 60)
        return minutes, seconds

def white():
    global colour, i

    root.destroy()

    colour = "white"          
    player1.colour = WHITE
    player2.colour = BLACK
    i = 0

def black():
    global colour, i

    root.destroy() 

    colour = "black"
    player2.colour = WHITE
    player1.colour = BLACK
    i = 1        

player1 = Player()
player2 = Player()

root = Tk()
root.geometry("580x280")
root.title("Che colore e' il giocatore a sinistra?")

blackButton = Button(root, text="Nero", command=black, bg="black", fg="white", height=HEIGHT, width=WIDTH)
blackButton.place(x=black_pos[x], y=black_pos[y])

whiteButton = Button(root, text="Bianco", command=white, bg="white", fg="black", height=HEIGHT, width=WIDTH)
whiteButton.place(x=white_pos[x], y=white_pos[y])

root.mainloop()

done = start = False

player1.time = 240
player2.time = 240
player1.time_coordinates = [190, 225]
player2.time_coordinates = [590, 225]

players = [player1,player2]
players_time_coordinates = [player1.time_coordinates, player2.time_coordinates]
time_players = [[3, 0], [3, 0]]

player1.background_colour = player2.colour
player2.background_colour = player1.colour

player1.sign_colour = player1.colour
player2.sign_colour = player2.colour

pygame.init()
size   = (880, 480)
screen = pygame.display.set_mode(size)
clock  = pygame.time.Clock()
font   = pygame.font.SysFont('Calibri', 50, True, False)

background_white_plays = pygame.image.load("white_sx_plays_white.png").convert() if colour == "white" else pygame.image.load("white_dx_plays_black.png").convert()
background_black_plays = pygame.image.load("white_sx_plays_black.png").convert() if colour == "white" else pygame.image.load("white_dx_plays_white.png").convert()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if not start:
                mode = 0 if event.key == pygame.K_s else 1 if event.key == pygame.K_m else 2 if event.key == pygame.K_l else mode
            if event.key == pygame.K_SPACE:
                if not start:
                    start = True
                else:
                    i = not i
            elif event.key == pygame.K_q:
                done = True 
            elif event.key == pygame.K_r:
                start = False
                i = 0 if colour == "white" else 1

    if not start:
        k = mod[mode]
        time = k*60
        player1.time = time
        player2.time = time
        time_players = [[k, 0], [k, 0]]
    else:
        player = players[i]
        time_players[i] = player.timer()

    time1 = font.render("{0:02}:{1:02}".format(time_players[0][0], time_players[0][1]), True, player1.background_colour)
    time2 = font.render("{0:02}:{1:02}".format(time_players[1][0], time_players[1][1]), True, player2.background_colour)

    screen.blit((background_white_plays if i else background_black_plays) if not start else (background_black_plays if i else background_white_plays), [0, 0])

    screen.blit(time1, players_time_coordinates[0])
    screen.blit(time2, players_time_coordinates[1])

    pygame.display.flip()
    clock.tick(100)

pygame.quit()