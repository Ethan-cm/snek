
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
print("Imports successful!") # If you see this printed to the console then installation was successful

window_w,window_h= 1000,1000



def drawsquare(leftx,rightx,bottomy,topy):
    glBegin(GL_QUADS)
    glVertex2f(leftx,bottomy)
    glVertex2f(rightx,bottomy)
    glVertex2f(rightx,topy)
    glVertex2f(leftx,topy)
    glEnd() #finish drawing this square

def square():
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd() #finish drawing this square 

def iterate():
    glViewport(0, 0, window_h, window_w)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, window_h, 0.0, window_w, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(228.0, 245.0, 0.0)
    square()
    glutSwapBuffers()

glutInit()      #initialize glut
glutInitDisplayMode(GLUT_RGBA) #set glut window to color
glutInitWindowSize(window_w, window_h) #resolution of the window
glutInitWindowPosition(0, 0) #position of the window
wind = glutCreateWindow("Snek is reale") #title of the window
glutDisplayFunc(showScreen) #
glutIdleFunc(showScreen)
glutMainLoop()