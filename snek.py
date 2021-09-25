
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
    #pygame.init()
    display = (1000,1000) #initializing 
    window  = pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #initialize screen with double buffering and opengl
    gluPerspective(45, display[0] / display[1], 1, 10)   
    glTranslatef(0,0,-5) #move the "camera" back

    while 1:
        for event in pygame.event.get(): #if x is clicked exit program
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) #clear the screen of color as well as positional data
        square()
        glTranslatef(-0.1,0,0)
        pygame.time.delay(100)
        pygame.display.flip() #flip the frame from the previously drawn one to the just now added one in the buffer

main()