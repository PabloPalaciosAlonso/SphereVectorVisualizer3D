"""
def stof(lista):
     Lista2=[]
     for elem in lista:
          Lista2+=[float(elem)]
     return Lista2

def readAllFrames(name):
     filein = open(name,"r")
     lines = []
     col = []
     count = 0
     for line in filein:
          if line[0]=="#":
               if count>0:
                    lines+=[col]
                    col = []
          else:
               col+=[stof(line.strip().split(' '))]
               count+=1
     return lines

"""
import numpy as np

def readAllFrames(name):
    with open(name, 'r') as f:
        content = f.read()
    frames = content.split('#')[1:]  # Split the content into frames, skip the first part if it's empty
    frames = [np.fromstring(frame, sep=' ') for frame in frames]  # Convert strings to numpy arrays
    return frames
