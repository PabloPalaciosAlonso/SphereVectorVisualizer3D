#!/usr/bin/env python3

"""
P. Palacios Alonso 2021-2022
Usage:
  SVV3D filename

Controls:

  *Movement:
    -Move the position of the camera with WASD and shift and control to up and down.
    -Rotate the animation in XYZ with 123 (clockwise) and 456 (anticlockwise).
    -With +- change the speed of the movement of the camera.

  *Frame control:
    -Press space and R to go to the next and to the previous frame respectively
    -Press B and T to go the first and to the last frame respectively

  *Others:
    -Press C to take a screenshot of the animation


File format:
  
  *Spheres: rx ry rz color radius
    -rxyz are the position of the center of each particle
    -radius and color are not compulsory to provide
        
  
  *Arrows:  rx ry rz vx vy vz color width
    -rxyz are the position of the bottom of the arrow
    -vxyz is the direction of the arrow
    -width and color are not compulsory to provide

  *Colors code
     -0 -> White
     -1 -> Green
     -2 -> Blue
     -3 -> Red
     -4 -> Orange
     -5 -> Purple
     -6 -> Grey

  *The end of the frame is indicated with #

  
Example
  #
  0 0 0 2 0
  0 0 0 2 2 2 2
  #
  0 1 0 2 0
  0 1 0 2 2 2 2
  #
  0 2 0 2 0
  0 2 0 2 2 2 2
"""

from pynput.keyboard import Key, Listener, KeyCode
from . import actions
from . import initAnimation as init
import threading

def on_press(key):
    options = {KeyCode.from_char('w'):actions.moveForward,
               KeyCode.from_char('s'):actions.moveBackward,
               KeyCode.from_char('a'):actions.moveLeft,
               KeyCode.from_char('d'):actions.moveRight,
               Key.shift:threading.Thread(target=actions.moveUp).start,
               Key.ctrl:threading.Thread(target=actions.moveDown).start,
               KeyCode.from_char('1'):actions.rotateXClockwise,
               KeyCode.from_char('2'):actions.rotateYClockwise,
               KeyCode.from_char('3'):actions.rotateZClockwise,
               KeyCode.from_char('4'):actions.rotateXAntiClockwise,
               KeyCode.from_char('5'):actions.rotateYAntiClockwise,
               KeyCode.from_char('6'):actions.rotateZAntiClockwise,
               Key.space:actions.nextFrame,
               KeyCode.from_char('r'):actions.previousFrame,
               KeyCode.from_char('b'):actions.firstFrame,
               KeyCode.from_char('t'):actions.lastFrame,
               KeyCode.from_char('+'):actions.increaseJump,
               KeyCode.from_char('-'):actions.decreaseJump,
               KeyCode.from_char('c'):actions.screenshot}
     
    if key in options.keys():
         options[key]()

def on_release(key):
    options = {Key.shift:actions.stopMovingUp,
               Key.ctrl:actions.stopMovingDown}

    if key in options.keys():
         options[key]()
         
def main():
    init.initializeAnimation()
    actions.moveForward()
    actions.moveBackward()
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()
        
if __name__ == "__main__":
    main()
    
