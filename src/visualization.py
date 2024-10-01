import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *

def init_window(width, height):
    pygame.init()
    pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
    glEnable(GL_DEPTH_TEST)