# SVV3D
Sphere Vector Visualizer in 3D

# Installing
```
python setup.py sdist
pip install dist/SVV3D-1.0.tar.gz
```

# Usage:
  SVV3D filename

# Controls:
  *Movement:
    -Move the position of the camera with WASD and shift and control to up and down.
    -Rotate the animation in XYZ with 123 (clockwise) and 456 (anticlockwise).
    -With +- change the speed of the movement of the camera.

  *Frame control:
    -Press space and R to go to the next and to the previous frame respectively
    -Press B and T to go the first and to the last frame respectively

  *Others:
    -Press C to take a screenshot of the animation

# File format:
  
  *Spheres: rx ry rz color radius
    -rx ry rz are the coordinates of the center of each particle
    -radius and color are not compulsory to provide
        
  
  *Arrows:  rx ry rz vx vy vz color width
    -rx ry rz are the position of the bottom of the arrow
    -vx vy vz is the direction of the vector
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

