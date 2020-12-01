import pygame
import serial

arduino = serial.Serial(port='COM5', baudrate=9600)

def num_map(x, in_min, in_max, out_min, out_max):
    return ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def message(value=0, header=0):
    mex_header = bin(header)
    mex_header = mex_header[2:]
    mex_text = bin(value)
    mex_text = mex_text[2:]
    for i in range(4 - len(mex_header)):
        mex_header = '0' + mex_header
    for i in range(8 - len(mex_text)):
        mex_text = '0' + mex_text
    mex = '0b' + mex_header + mex_text    
    return  int(mex, 0)

headers = {
    "lstick" : 1,
    "rstick" : 2,
    "l2" : 3,
    "r2" : 4,
    "l1" : 5,
    "r1" : 6,
    "l3" : 7,
    "r3" : 8,
    "triangolo" : 9,
    "quadrato" : 10,
    "croce" : 11,
    "cerchio" : 12
}

pygame.init()

done = False
state = False
clock = pygame.time.Clock()

pygame.joystick.init()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    joystick_count = pygame.joystick.get_count()

    if joystick_count==0:
        print("nessun controller")

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)
            if i==4:
                mex = message(int(num_map(axis, -1.0, 1.0, 0.0, 256.0)), headers.get("r2"))
                print(mex)

        buttons = joystick.get_numbuttons()
        for i in range(buttons):
            button = joystick.get_button(i)
            if button==1 and i==12:
                done = True

        # hats = joystick.get_numhats()
        # for i in range(hats):
        #     hat = joystick.get_hat(i)
    clock.tick(120)

pygame.quit()