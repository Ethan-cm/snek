
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
    NONE = (0,0,0)

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

class body: #class that contains all the data and functions for the rendering of the body
    verticesstructure = [ [-1, -2,  1, -2,  1, -1,  -1, -1], [-1, -4,  1, -4,  1, -2,  -1, -2] ] #initial placement of the two starting body parts
    bodylength = 3 #amount of segments the body will have initially, will be increased every time the body is extended


    def update(self, vertices,translationtrack): #function is run every render loop, updates the list of lists of vertices
        intvertices = []
        if translationtrack != [0,0]: #if the head is moving we update the vertices, if stationary do not
            for element in vertices:
                intvertices.append(int(element))
                    #take the new vertices and multiply them by ten, then convert to integers for the iterative process to work
            self.verticesstructure.append(intvertices)
            
            if self.bodylength == (len(self.verticesstructure)): # if the body length is maintained (food not eaten) then we need to get rid of the first element in the original list to keep the length
                self.verticesstructure.pop(0) 


    def render(self):
        #first we change the data into something more easily rendered
        
        vertexstruct = self.verticesstructure   
        for vertexset in range(len(vertexstruct)):
            tupleform = ( 
                (vertexstruct[vertexset][0],vertexstruct[vertexset][1]),
                (vertexstruct[vertexset][2],vertexstruct[vertexset][3]),
                (vertexstruct[vertexset][4],vertexstruct[vertexset][5]),
                (vertexstruct[vertexset][6],vertexstruct[vertexset][7])
            )
            glBegin(GL_QUADS)
            for tupleset in tupleform: #loop iterates over the number of sets of tuples
               for edge in snake.edges: #loop iterates over the 
                    for vertex in edge: #loop iterates over the vertices in the body
                        glVertex2fv(tupleform[vertex])
            glEnd()
            print("tupleform\n",tupleform)



class border:
    vertices = (
        (-18,-18),
        (18,-18),
        (18,18),
        (-18,18)

    )
    edges = (
        (0,1),
        (1,2),
        (2,3),
        (3,0)
    )

def square(vertices):
    snake.vertices = (
        (vertices[0],vertices[1]),
        (vertices[2],vertices[3]),
        (vertices[4],vertices[5]),
        (vertices[6],vertices[7])
    )

    glBegin(GL_QUADS)
    for surface in surfaces: #initially pointless, will be used later when the snake bends
        glColor3fv((255,139,69))
    for edge in snake.edges:
        for vertex in edge:
            glVertex2fv(snake.vertices[vertex])
    glEnd()
   
def borderdraw():

    glBegin(GL_LINES)
    for edge in border.edges:
        for vertex in edge:
            glVertex2fv(border.vertices[vertex])
    glEnd()

def initialscaleobjects(time):
    if time == 0: #at time = 0 we scale our object to the new size 
        glScale(0.1, 0.1, 1)
        time = time + 1
        pygame.display.flip()
        variables.isscaled = 1
        return 1

def scaleobjects(x,y,z):
    glScale(x,y,z)
#    pygame.display.flip()

def movement(direction): #function for
    #glTranslatef(direction[0],direction[1],direction[2]) #movement function, defined as such to return a dataset of the current position of the object
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
    elif direction == directions.NONE:
        updatevertices = [0,0]
        return updatevertices

def updateheadposition(translationtracker,vertices):
    if translationtracker == [0,-0.1]: #change the vertices that correspond to the position of the head in vector space. Really shoddy solution but its readable and thats what I care about at the moment
            vertices[1] = vertices[1] - 1 #y
            vertices[3] = vertices[3] - 1 #y
            vertices[5] = vertices[5] - 1#y
            vertices[7] = vertices[7] - 1 #y
    elif translationtracker == [0,0.1]: #up
            vertices[1] = vertices[1] + 1 #y
            vertices[3] = vertices[3] + 1  #y
            vertices[5] = vertices[5] + 1  #y
            vertices[7] = vertices[7] + 1  #y
    elif translationtracker == [-0.1,0]: #left x coordinates negative increase
            vertices[0] = vertices[0] - 1  #x
            vertices[2] = vertices[2] - 1 #x
            vertices[4] = vertices[4] - 1 #x
            vertices[6] = vertices[6] - 1 #x
    elif translationtracker == [0.1,0]: #right x coordinates positive increase
            vertices[0] = vertices[0] + 1 #x
            vertices[2] = vertices[2] + 1 #x
            vertices[4] = vertices[4] + 1 #x
            vertices[6] = vertices[6] + 1 #x
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
                direction = directions.NONE
    return direction

def main():
    display = (1000,1000) #initializing 
    window  = pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #initialize screen with double buffering and opengl
    gluPerspective(45, display[0] / display[1], 1, 50)  #set the perspective necessary to see everything at a proper plane
    glTranslatef(0,0,-45) #move the "camera" back
    glShadeModel(GL_SMOOTH)

    direction = (0,0,0)
    translationtrack = [0,0]
    initialvertices = [-1,-1,1,-1,1,1,-1,1] #keep track of positions of the vertices in the head of the snake, allow for collision detection 
    vertex = [0,0,0,0,0,0,0,0]
    snakebody = body()#render the rest of the body

    while 1: #### MAIN LOOP ##############################################################################

        direction = getdirection(direction)
        translationtrack = movement(direction) #move the object and track the direction it is going in
        vertex = updateheadposition(translationtrack, initialvertices) #update the position of the head of the snake in vector space


        glClearColor(0, 0, 0, 1) # specifies color for the background
        glColor3f(255,139,69)
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) #clear the screen of color as well as positional data


        square(vertex) # render the square
        snakebody.update(vertex,translationtrack)#render the rest of the body
        print("Vertex\n",vertex)
        snakebody.render()
        #glLoadIdentity()
        #scaleobjects(0.01,0.01,1)

        pygame.time.delay(333)
        pygame.display.flip() #flip the frame from the previously drawn one to the just now added one in the buffer


#########################################END OF MAIN LOOP ##############################################
main()