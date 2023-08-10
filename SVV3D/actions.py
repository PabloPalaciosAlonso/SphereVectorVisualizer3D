from . import initAnimation as init
import vpython as vp
from math import sin, cos
import time
import os

sqrt3 = 1.7320508075688

is_w_pressed     = False
is_s_pressed     = False
is_a_pressed     = False
is_d_pressed     = False
is_ctrl_pressed  = False
is_shift_pressed = False

is_1_pressed     = False
is_2_pressed     = False
is_3_pressed     = False
is_4_pressed     = False
is_5_pressed     = False
is_6_pressed     = False


# Display a frame of the animation
def setPos():
    nParticles = len(init.data[init.frame])
    for i in range(nParticles):
        [x, y, z] = init.data[init.frame][i][0:3]
        init.particles[i].pos = vp.vector(x,y,z)
        init.lbox = max(2*abs(x), 2*abs(y), 2*abs(z), init.lbox)
        if (len(init.data[init.frame][i])>5):
            [ax, ay, az] = init.data[init.frame][i][3:6]
            init.particles[i].axis = vp.vector(ax, ay, az)
            init.lbox = max(2*abs(x+ax), 2*abs(y+ay), 2*abs(z+az), init.lbox)
            
# Given a rotation matrix rotates the posiiton of the camera
def rotateCamera(rotationMatrix):
    [v1,v2,v3] = rotationMatrix
    axis = init.scene.camera.axis
    pos  = init.scene.camera.pos
    up   = init.scene.camera.up
    init.scene.camera.axis = vp.vector(vp.dot(v1,axis),
                                       vp.dot(v2,axis),
                                       vp.dot(v3,axis))
    init.scene.camera.pos =  vp.vector(vp.dot(v1,pos),
                                       vp.dot(v2,pos),
                                       vp.dot(v3,pos))
    init.scene.camera.up =   vp.vector(vp.dot(v1,up),
                                       vp.dot(v2,up),
                                       vp.dot(v3,up))

######################## Actions that move the camera #####################################

def moveForward():
    df = init.lbox*init.jump
    cameraPos = init.scene.camera.pos
    cameraAxis = init.scene.camera.axis
    direc = vp.norm(cameraAxis)
    init.scene.camera.pos+=df*direc
    init.scene.camera.axis=direc*init.lbox*sqrt3
            
def moveBackward():
    df = init.lbox*init.jump
    cameraPos = init.scene.camera.pos
    cameraAxis = init.scene.camera.axis
    direc = vp.norm(cameraAxis)
    init.scene.camera.pos-=df*direc        
    init.scene.camera.axis=direc*init.lbox*sqrt3
            
def moveLeft():
    df = init.lbox*init.jump
    cameraPos = init.scene.camera.pos
    cameraUp = init.scene.up
    cameraAxis = init.scene.camera.axis
    direc = vp.norm(vp.cross(cameraUp,cameraAxis))
    init.scene.camera.pos+=df*direc
            
def moveRight():
    df = init.lbox*init.jump
    cameraUp = init.scene.up
    cameraAxis = init.scene.camera.axis
    direc = vp.norm(vp.cross(cameraUp,cameraAxis))
    init.scene.camera.pos-=df*direc
            
def moveUp():
    global is_shift_pressed
    is_shift_pressed = True
    while is_shift_pressed:
        df = init.lbox*init.jump
        cameraPos = init.scene.camera.pos
        cameraUp =  init.scene.up
        direc = vp.norm(cameraUp)
        init.scene.camera.pos+=df*direc
        time.sleep(0.04)
    
def moveDown():
    global is_ctrl_pressed
    is_ctrl_pressed = True
    while is_ctrl_pressed:
        df = init.lbox*init.jump
        cameraUp = init.scene.up
        direc = vp.norm(cameraUp)
        init.scene.camera.pos-=df*direc
        time.sleep(0.04)

def stopMovingUp():
    global is_shift_pressed
    is_shift_pressed = False

def stopMovingDown():
    global is_ctrl_pressed
    is_ctrl_pressed = False


######################## Actions that rotate the camera #####################################

def rotateXClockwise():
    dtheta = init.jump
    v1 = vp.vector(1,  0          , 0          )
    v2 = vp.vector(0,  cos(dtheta), sin(dtheta))
    v3 = vp.vector(0, -sin(dtheta), cos(dtheta))
    rotateCamera([v1,v2,v3])
    l = init.scene.lights[0]
    l.direction = -init.scene.camera.axis
    
def rotateYClockwise():
    dtheta = init.jump
    v1 = vp.vector(cos(dtheta), 0, -sin(dtheta))
    v2 = vp.vector(0          , 1,  0          )
    v3 = vp.vector(sin(dtheta), 0,  cos(dtheta))
    rotateCamera([v1,v2,v3])
    l = init.scene.lights[0]
    l.direction = -init.scene.camera.axis
    
def rotateZClockwise():
    dtheta = init.jump
    v1 = vp.vector( cos(dtheta), sin(dtheta), 0)
    v2 = vp.vector(-sin(dtheta), cos(dtheta), 0)
    v3 = vp.vector( 0          , 0          , 1)
    rotateCamera([v1,v2,v3])
    l = init.scene.lights[0]
    l.direction = -init.scene.camera.axis     
         
def rotateXAntiClockwise():
    dtheta = -init.jump
    v1 = vp.vector(1,  0          , 0          )
    v2 = vp.vector(0,  cos(dtheta), sin(dtheta))
    v3 = vp.vector(0, -sin(dtheta), cos(dtheta))
    rotateCamera([v1,v2,v3])
    l = init.scene.lights[0]
    l.direction = -init.scene.camera.axis
            
def rotateYAntiClockwise():
    dtheta = -init.jump
    v1 = vp.vector(cos(dtheta), 0, -sin(dtheta))
    v2 = vp.vector(0          , 1,  0          )
    v3 = vp.vector(sin(dtheta), 0,  cos(dtheta))
    rotateCamera([v1,v2,v3])
    l = init.scene.lights[0]
    l.direction = -init.scene.camera.axis
          
def rotateZAntiClockwise():
        dtheta = -init.jump
        v1 = vp.vector( cos(dtheta), sin(dtheta), 0)
        v2 = vp.vector(-sin(dtheta), cos(dtheta), 0)
        v3 = vp.vector( 0          , 0          , 1)
        rotateCamera([v1,v2,v3])
        l = init.scene.lights[0]
        l.direction = -init.scene.camera.axis
        
################################## Actions to change the frame ##################################

def nextFrame():
    if init.frame<len(init.data)-1:
        if init.record:            
            init.scene.capture("frame_"+str(init.frame))
        init.frame+=1
        setPos()
        
def previousFrame():
    if init.frame>0:
        init.frame-=1
        setPos()

# Moves the animation to the last frame
def lastFrame():
    init.frame = len(init.data)-1
    setPos()

# Moves the animation to the first frame
def firstFrame():
    init.frame = 0
    setPos()

################################## Other actions ##################################

# Increases the jump size
def increaseJump():
    init.jump*=1.1

# Decreases the jump size
def decreaseJump():
    init.jump/=1.1

# Takes a screenshot of the scene
def screenshot():
    if not is_ctrl_pressed:
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        print("Taking a screenshot of the frame "+str(init.frame))
        init.scene.capture("screenshots/shot_"+str(init.nscreenshots))
        init.nscreenshots+=1
    


