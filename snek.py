
import OpenGL, sys, pygame, time
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from pygame.display import *
pygame.init()
print("Imports successful!") # just a check to see if libraries functioned

class directions:
    DOWN = (0,-2,0)
    UP = (0,2,0)
    LEFT = (-2,0,0)
    RIGHT = (2,0,0)

isscaled = 0

class variables:
    yellow = ( 235 , 219 ,52 )
    blue   = ( 52 , 61 , 235 )
    isscaled = 0

#head vertices and edges
class snake:
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

surfaces = ( 0,1,2,3 ) #draw a surface across the border to allow us to see the map boundary


class border:
    vertices = (
#        (-18,-18),
#        (18,-18),
#        (18,18),
#        (-18,18)
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

def square():

    glBegin(GL_QUADS)
    for surface in surfaces: #initially pointless, will be used later when the snake bends
        glColor3fv((255,139,69))
    for edge in snake.edges:
        for vertex in edge:
            glVertex2fv(snake.vertices[vertex])
    glEnd()
    variables.isscaled = initialscaleobjects(variables.isscaled)    #scales the object to 0.1 of its original size, puts the vertices at -0.1,-0.1 to 0.1, 0.1
   
def borderdraw():

    glBegin(GL_LINES)
    for edge in border.edges:
        for vertex in edge:
            glVertex2fv(border.vertices[vertex])
    glEnd()
    #glScale(0.1, 0.1, 1)
    #scaleobjects()
    #variables.isscaled = initialscaleobjects(variables.isscaled)    #scales the object to 0.1 of its original size, puts the vertices at -0.1,-0.1 to 0.1, 0.1

def initialscaleobjects(time):
    if time == 0: #at time = 0 we scale our object to the new size 
        glScale(0.1, 0.1, 1)
        time = time + 1
        pygame.display.flip()
        variables.isscaled = 1
        return 1

def scaleobjects():
    glScale(0.1, 0.1, 1)
    pygame.display.flip()

def movement(direction): #function for
    glTranslatef(direction[0],direction[1],direction[2]) #movement function, defined as such to return a dataset of the current position of the object
    updatevertices = [0,0] #xyz
    #logic statement that allows us to maintain an idea of where the head of the snake is positioned. This is used to detect collisions with objects as well as the edges of the screen
    if direction == directions.DOWN: #down
        updatevertices = [0,-0.1]
        return updatevertices
    elif direction == directions.UP:  #up
        updatevertices = [0,0.1]
        return updatevertices
    elif direction == directions.LEFT: #left
        updatevertices = [-0.1,0]
        return updatevertices
    elif direction == directions.RIGHT: #right
        updatevertices = [0.1,0]
        return updatevertices

#def checkcollision(vertex): #check collision with the window boundary, boundaries at 18.1 positive and negative boundaries
    #need to check collosion of 
 #   if 

def updateheadposition(translationtracker,vertices):
    if translationtracker == [0,-0.1]: #down #reduce the vertices that correspond to 
            vertices[1] = vertices[1] + directions.DOWN[1] #y
            vertices[3] = vertices[3] + directions.DOWN[1] #y
            vertices[5] = vertices[5] + directions.DOWN[1] #y
            vertices[7] = vertices[7] + directions.DOWN[1] #y
    elif translationtracker == [0,0.1]: #up
            vertices[1] = vertices[1] + directions.UP[1] #y
            vertices[3] = vertices[3] + directions.UP[1]  #y
            vertices[5] = vertices[5] + directions.UP[1]  #y
            vertices[7] = vertices[7] + directions.UP[1]  #y
    elif translationtracker == [-0.1,0]: #left x coordinates negative increase
            vertices[0] = vertices[0] + directions.LEFT[0]  #x
            vertices[2] = vertices[2] + directions.LEFT[0] #x
            vertices[4] = vertices[4] + directions.LEFT[0] #x
            vertices[6] = vertices[6] + directions.LEFT[0] #x
    elif translationtracker == [0.1,0]: #right x coordinates positive increase
            vertices[0] = vertices[0] + directions.RIGHT[0] #x
            vertices[2] = vertices[2] + directions.RIGHT[0] #x
            vertices[4] = vertices[4] + directions.RIGHT[0] #x
            vertices[6] = vertices[6] + directions.RIGHT[0] #x
    return vertices


def getdirection(direction):
    for event in pygame.event.get(): #if x is clicked exit program
        if event.type == pygame.QUIT: #input capture
            pygame.quit
            quit()
        if event.type == pygame.KEYDOWN: #executes when a key is pressed down,left right or up and changes the direction variable for input to be sent to openGL
            if event.key == pygame.K_LEFT:
                direction = directions.LEFT
            if event.key == pygame.K_RIGHT:
                direction = directions.RIGHT
            if event.key == pygame.K_UP:
                direction = directions.UP
            if event.key == pygame.K_DOWN:
                direction = directions.DOWN
            if event.key == pygame.K_SPACE:
                direction = (0,0,0)
    return direction

def main():
    display = (1000,1000) #initializing 
    window  = pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #initialize screen with double buffering and opengl
    gluPerspective(45, display[0] / display[1], 1, 10)  #set the perspective necessary to see everything at a proper plane
    glTranslatef(0,0,-5) #move the "camera" back
    glShadeModel(GL_SMOOTH)

    direction = (0,0,0)
    translationtrack = [0,0]
    initialvertices = [-0.1,-0.1,0.1,-0.1,0.1,0.1,-0.1,0.1] #keep track of positions of the vertices in the head of the snake, allow for collision detection 
    lastvertices = [0,0,0,0,0,0,0,0]
    vertex = [0,0,0,0,0,0,0,0]

    while 1: #### MAIN LOOP ##############################################################################


        direction = getdirection(direction)

        translationtrack = movement(direction) #move the object and track the direction
        vertex = updateheadposition(translationtrack, initialvertices) #

        glClearColor(0, 0, 0, 1) # specifies color for the background
        glColor3f(255,139,69)
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) #clear the screen of color as well as positional data

        square() # rendersquare
#        glLoadIdentity()
        glPushMatrix() #
        glLoadIdentity()
        borderdraw()
        glPopMatrix()
        #scaleobjects()
        #initialscaleobjects(variables.isscaled)

        ######test box
        #
        #
        #
        #
        #

        pygame.time.delay(250)
        pygame.display.flip() #flip the frame from the previously drawn one to the just now added one in the buffer


#########################################END OF MAIN LOOP ##############################################
main()