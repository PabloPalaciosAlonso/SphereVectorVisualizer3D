# SVV3D
Sphere Vector Visualizer in 3D (SVV3D) is a tool for visualizing spheres and vectors in a 3D environment.

## Installation

Clone this repository:

```bash
git clone git@github.com:PabloPalaciosAlonso/SphereVectorVisualizer3D.git
```

Navigate to the cloned directory:

```bash
cd SphereVectorVisualizer3D
```

Then use the following commands to install SVV3D:

```bash
python setup.py sdist
pip install dist/SVV3D-1.0.tar.gz
```

## Usage
To use SVV3D, simply pass a filename to the program:

```bash
SVV3D <filename>
```

## Controls
### Movement:
- Use the `W`, `A`, `S`, and `D` keys to move the camera.
- Use `Shift` and `Ctrl` to move the camera up and down, respectively.
- Use the `1`, `2`, and `3` keys to rotate the animation clockwise along the X, Y, and Z axes, respectively.
- Use the `4`, `5`, and `6` keys to rotate the animation anticlockwise along the X, Y, and Z axes, respectively.
- Use the `+` and `-` keys to increase and decrease the speed of the camera movement, respectively.

### Frame Control:
- Use the `Space` key to advance to the next frame.
- Use the `R` key to return to the previous frame.
- Use the `B` key to jump to the first frame.
- Use the `T` key to jump to the last frame.

### Others:
- Use the `C` key to take a screenshot of the animation.

## File Format
### Spheres
Each sphere is defined by a line in the following format:
```
rx ry rz color radius
```
- `rx`, `ry`, `rz`: Coordinates of the center of the sphere
- `color`: (optional) Color code of the sphere
- `radius`: (optional) Radius of the sphere

### Arrows
Each arrow is defined by a line in the following format:
```
rx ry rz vx vy vz color width
```
- `rx`, `ry`, `rz`: Position of the base of the arrow
- `vx`, `vy`, `vz`: Direction vector of the arrow
- `color`: (optional) Color code of the arrow
- `width`: (optional) Width of the arrow

### Color Codes
- `0`: White
- `1`: Green
- `2`: Blue
- `3`: Red
- `4`: Orange
- `5`: Purple
- `6`: Grey

The end of a frame is indicated with a `#` symbol.

