import numpy as np
import sys
import argparse
import vpython as vp
from . import color
import re

scene = None
frame = 0
lbox = 0
jump = 0.025
particles = []
maxNParticles = 0
data = []
filename = ""
windowSize = (800,700)
nscreenshots = 0

""" TODO: Solve errors related with animations with different number of particles per frame """


def readCMArguments():
    global filename
    global windowSize
    inputArguments = argparse.ArgumentParser()
    inputArguments.add_argument('-ws', type = float, nargs = 2, default = (800, 700))
    inputArguments.add_argument('file', nargs = 1)
    arguments = inputArguments.parse_args()
    windowSize = arguments.ws
    filename = arguments.file[0]

def readAllFrames():
     global data
     with open(filename, 'r') as f:
          content = f.read()
     content = re.sub(r'#.*', '#', content)    
     frames = content.split('#')[1:]  # Split the content into frames, skip the first part if it's empty
     frames = [np.array([np.fromstring(row, sep=' ') for row in frame.strip().split('\n')]) for frame in frames]

     # Check that all frames have the same length
     frame_len = len(frames[0])
     for i, frame in enumerate(frames[1:], start=1):  # Skip the first frame, because we're using its length as the base
          if len(frame) != frame_len:
               raise ValueError(f"Frame {i} has a different number of elements ({len(frame)}) than the first frame ({frame_len}).")
          
     data = frames


def setMaxNParticles():
    global maxNParticles
    maxNParticles = len(data[0])

def createScene():
    global scene
    scene = vp.canvas(width = windowSize[0], height = windowSize[1], autoscale = False)
    scene.userzoom = False
    scene.lights[1].visible = False
    
def createParticleList():
    global particles
    global lbox
    global scene
    firstFrame = data[0]
    for i in range(maxNParticles):
        [x,y,z] = firstFrame[i][:3]
        nInputs = len(firstFrame[i])
        if nInputs<6: #Sphere
            radius = 1 if nInputs==3 else firstFrame[i][3]    
            colorId = 0 if nInputs<5 else firstFrame[i][4]
            particles.append(vp.sphere(pos = vp.vector(x,y,z), radius = radius,
                                       color = color[colorId]))
            lbox = max(max(2*abs(x),2*abs(y),2*abs(z))+2*radius,lbox)
        else: #Arrow
            [axisx, axisy, axisz] = firstFrame[i][3:6]
            arrowLength = np.sqrt(axisx*axisx+axisy*axisy+axisz*axisz)
            colorId = 1 if nInputs == 7 else firstFrame[i][6]
            arrowWidth = arrowLength/17.5 if nInputs < 8 else firstFrame[i][7]
            particles.append(vp.arrow(pos = vp.vector(x,y,z),
                                      axis = vp.vector(axisx, axisy, axisz),
                                      color = color[colorId], shaftwidth=arrowWidth))
            maxpos = max(max(x+axisx,y+axisy,z+axisz),-min(x+axisx,y+axisy,z+axisz), lbox)
    scene.camera.pos = vp.vector(0,0,0.9*lbox)
    
def initializeAnimation():
    readCMArguments()
    readAllFrames()
    setMaxNParticles()
    createScene()
    createParticleList()

