
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from time import sleep
print("Imports successful!") # If you see this printed to the console then installation was successful


translation = 0
w,h= 500,500
def square():
    glBegin(GL_QUADS)
    glVertex2f(100, 100) #sets the vertices of the window as it is drawn, along the lines
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500) #sets the bounds of the rendering window
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    square()
    glutSwapBuffers()

def newsquare():
    glBegin(GL_QUADS)
    glVertex2f(100+translation, 100+translation) #sets the vertices of the window as it is drawn, along the lines
    glVertex2f(200+translation, 100+translation) #sets the vertices of the window as it is drawn,
    glVertex2f(200+translation, 200+translation)
    glVertex2f(100+translation, 200+translation)
    glEnd()

def newscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    newsquare()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Snake coding practice, moving square no input")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
while translation > 300 :
    sleep(0.1)
    glutDisplayFunc(newscreen)
    translation =+ 1
glutIdleFunc(newscreen)
glutMainLoop()
