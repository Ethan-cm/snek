
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
    (-1,-1),
    (1,-1),
    (1,1),
    (-1,1)
)

edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0)
)

surfaces = ( 0,1,2,3 ) #draw a surface across

def square():

    glBegin(GL_QUADS)
    for surface in surfaces: #initially pointless, will be used later when the snake bends
        glColor3fv((255,139,69))
    for edge in edges:
        for vertex in edge:
            glVertex2fv(vertices[vertex])
    glEnd()

def initialscaleobjects(time):
    print(time)
    if time == 0: #at time = 0 we scale our object to the new size 
        glScale(0.1, 0.1, 1)
        time = time + 1
        pygame.display.flip()
        return 1


def main():
    display = (1000,1000) #initializing 
    window  = pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #initialize screen with double buffering and opengl
    gluPerspective(45, display[0] / display[1], 1, 10)   
    glTranslatef(0,0,-5) #move the "camera" back
    glShadeModel(GL_SMOOTH)

    isscaled = 0
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

        #main rendering loop
        glClearColor(0, 0, 0, 1) # specifies color for the background
        glColor3f(255,139,69)
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) #clear the screen of color as well as positional data

        
        square() # rendersquare
        isscaled = initialscaleobjects(isscaled)    #scales the object to 0.1 of its original size, puts the vertices at -0.1,-0.1 to 0.1, 0.1


        glTranslatef(direction[0],direction[1],direction[2]) #movement

        pygame.time.delay(10)
        pygame.display.flip() #flip the frame from the previously drawn one to the just now added one in the buffer


#########################################END OF MAIN LOOP ##############################################
main()