
import OpenGL, sys, pygame, time
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from pygame.display import *
pygame.init()
print("Imports successful!") # just a check to see if libraries functioned

#colors for items in game

yellow = ( 235 , 219 ,52 )
blue   = ( 52 , 61 , 235 )

vertices = (
    (1,1),
    (2,1),
    (2,2),
    (1,2)
)

edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0)
)

def square():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex2fv(vertices[vertex])
    glEnd()


def main():

    display = (1000,1000) #initializing 
    window  = pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #initialize screen with double buffering and opengl
    gluPerspective(40, display[0] / display[1], 1, 10)
    
    glTranslatef(0,0,-5)
    color = (255,0,0)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
        square()
        pygame.display.flip()

main()