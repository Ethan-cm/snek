
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
    glBegin(GL_QUADS)
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
    time = 0
    direction = (0,0,0)
    while 1: #### MAIN LOOP ##############################################################################
        for event in pygame.event.get(): #if x is clicked exit program
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
            if event.type == pygame.KEYDOWN: #executes when a key is pressed down
                if event.key == pygame.K_LEFT:
                    direction = (-0.1,0,0)
                if event.key == pygame.K_RIGHT:
                    direction = (0.1,0,0)
                if event.key == pygame.K_UP:
                    direction = (0,0.1,0)
                if event.key == pygame.K_DOWN:
                    direction = (0,-0.1,0)
                if event.key == pygame.K_SPACE:
                    direction = (0,0,0)

        #put input capture here, as the way the object is draw will be dependant on the way the object has been turned




        #main rendering pipe
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) #clear the screen of color as well as positional data
        square()
        if time == 0: #at time = 0 we scale our object to the new size 
            glScale(0.5, 0.5, 1)
            time = time + 1
            pygame.display.flip()

        glTranslatef(direction[0],direction[1],direction[2])

        pygame.time.delay(10)
        pygame.display.flip() #flip the frame from the previously drawn one to the just now added one in the buffer


#########################################END OF MAIN LOOP ##############################################
main()