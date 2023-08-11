import numpy as np
import sys
import os
import argparse
import vpython as vp
from . import color
import re

scene         = None
frame         = 0
lbox          = 0
jump          = 0.025
particles     = []
maxNParticles = 0
data          = []
filename      = ""
windowSize    = (800,700)
nscreenshots  = 0
opacity       = 1

record = False

#Record the animation for the moment is not allowed, because the animation
#runs in a browser and saving the images for making the video
#implies to download (and hence set where you want to download) each frame of the video
#One way to have the animation is to usa a screen capturer


""" TODO: Solve errors related with animations with different number of particles per frame """


def readCMArguments():
    global filename
    global windowSize
    global opacity
    global record
    global opacity
    
    inputArguments = argparse.ArgumentParser()
    inputArguments.add_argument('--WindowSize' , type = float, nargs = 2, default = (800, 700))
    inputArguments.add_argument('--record'     , action='store_true')
    
    inputArguments.add_argument('file', nargs = 1)

    arguments  = inputArguments.parse_args()
    windowSize = arguments.WindowSize
    filename   = arguments.file[0]
    record     = arguments.record

    if record:
        print("WARNING: The record option is not availble for the moment")
        record = False
        
    if record:
        if not os.path.exists("tmp"):
            os.makedirs("tmp")
        
def readAllFrames():
    global data
    global opacity
    
    with open(filename, 'r') as f:
        content = f.read()

    # Read the opacity of the spheres
    match = re.search(r'#?SPHERE OPACITY ([+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)', content)
    if match:
        opacity = float(match.group(1))
        if opacity < 0 or opacity > 1:
            raise ValueError("The opacity of the spheres must be a value between 0 and 1")
    content = re.sub(r'#.*', '#', content)    
    frames = content.split('#') # Split the content into frames
    if len(frames)>1:
        frames  = frames[1:]  
    frames  = [[np.fromstring(row, sep=' ') for row in frame.strip().split('\n')] for frame in frames]
    if len(frames)>1:
        # Check that all frames have the same length
        frame_len     = 0
        firstFrame_id = 0
        while frame_len == 0:
            #print(frames[firstFrame_id])
            frame_len = frames[firstFrame_id][0].size
            #if frames[firstFrame_id] == '\n':
            #    frame_len = 0
            #print(frame_len)
            firstFrame_id += 1

        for i, frame in enumerate(frames[firstFrame_id:], start=firstFrame_id):
            if frame[0].size != frame_len:
                raise ValueError(f"Frame {i} has a different number of elements ({len(frame)}) than the first frame ({frame_len}).")
        data = frames[firstFrame_id-1:]        
    else:
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
    global opacity
    firstFrame = data[0]
    for i in range(maxNParticles):
        [x,y,z] = firstFrame[i][:3]
        nInputs = len(firstFrame[i])
        if nInputs<6: #Sphere
            radius = 1 if nInputs==3 else firstFrame[i][3]    
            colorId = 0 if nInputs<5 else firstFrame[i][4]
            particles.append(vp.sphere(pos = vp.vector(x,y,z), radius = radius,
                                       color = color[colorId%(len(color.keys()))], opacity=opacity))
            lbox = max(max(2*abs(x),2*abs(y),2*abs(z))+2*radius,lbox)
        else: #Arrow
            [axisx, axisy, axisz] = firstFrame[i][3:6]
            arrowLength = np.sqrt(axisx*axisx+axisy*axisy+axisz*axisz)
            colorId = 1 if nInputs == 6 else firstFrame[i][6]
            arrowWidth = arrowLength/17.5 if nInputs < 8 else firstFrame[i][7]
            particles.append(vp.arrow(pos = vp.vector(x,y,z),
                                      axis = vp.vector(axisx, axisy, axisz),
                                      color = color[colorId%len(color.keys())],
                                      shaftwidth =   arrowWidth,
                                      headwidth  = 3*arrowWidth,
                                      headlength = 4*arrowWidth))
            maxpos = max(max(x+axisx,y+axisy,z+axisz),-min(x+axisx,y+axisy,z+axisz), lbox)
    scene.camera.pos = vp.vector(0,0,0.9*lbox)
    
def initializeAnimation():
    readCMArguments()
    readAllFrames()
    setMaxNParticles()
    createScene()
    createParticleList()

