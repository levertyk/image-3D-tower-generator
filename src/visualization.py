import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *

def init_window(width, height):
    pygame.init()
    pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
    glEnable(GL_DEPTH_TEST)
    
def render_towers(towers):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for tower in towers:
        glBegin(GL_QUADS)
        #TODO draw towers
        glEnd()
        
def main_loop(towers):
    init_window(800, 600)
    while True:
        render_towers(towers)
        pygame.time.wait(10) #max frame rate is 10 per second for rendering