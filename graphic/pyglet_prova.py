import pyglet
import GraphicEngineV1_pyglet as graphic
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
colour = [255, 255, 255]

WIDTH, HEIGHT = 800, 800
WIDTH_FLOAT  = float(WIDTH)
HEIGHT_FLOAT = float(HEIGHT)

center = np.array((WIDTH_FLOAT / 2, HEIGHT_FLOAT / 2, 0.0))

radius = 5
line_width = 1
side = 300.0

window = pyglet.window.Window(WIDTH, HEIGHT)
pyglet.clock.set_fps_limit(100)

cube = graphic.Cube(center, center, radius, colour, side, line_width, WHITE)

@window.event
def on_draw():
	window.clear()
	batch = graphic.draw_solid(cube)
	batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.Q:
        event_loop.exit()

event_loop = pyglet.app.EventLoop()

event_loop.run()

# import pyglet
# pyglet.options['debug_gl'] = False
# from pyglet.gl import *

# Direct OpenGL commands to this window.
# window = pyglet.window.Window(1280, 720, resizable=True)
# pyglet.clock.set_fps_limit(100)

# @window.event
# def on_draw():
#     glClear(GL_COLOR_BUFFER_BIT)
#     glLoadIdentity()
#     glBegin(GL_TRIANGLES)
#     glVertex2f(0, 0)
#     glVertex2f(window.width, 0)
#     glVertex2f(window.width, window.height)
#     glEnd()

# @window.event
# def on_resize(width, height):
#     glViewport(0, 0, width, height)
#     glMatrixMode(gl.GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0, width, 0, height, -1, 1)
#     glMatrixMode(gl.GL_MODELVIEW)

# @window.event
# def on_key_press(symbol, modifiers):
#     if symbol == pyglet.window.key.Q:
#         event_loop.exit()

# event_loop = pyglet.app.EventLoop()
# event_loop.run()