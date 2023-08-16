# SVV3D
Sphere Vector Visualizer in 3D (SVV3D) is a tool for visualizing spheres and vectors in a 3D environment.

![Particles with an internal reference frame](https://github.com/PabloPalaciosAlonso/SphereVectorVisualizer3D/blob/master/screenshots/shot_1.png)

![Particles with an arrow inside them indicating a specific direction in the particles frame](https://github.com/PabloPalaciosAlonso/SphereVectorVisualizer3D/blob/master/screenshots/shot_2.png)


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

To use a different window size, add the  -WindowSize option followed by the desired width and height to the command line:

```bash
SVV3D <filename> -WindowSize width height
```

Remember, 'filename', 'width', 'height', and 'opacity' are placeholders and should be replaced with your actual file name, desired dimensions, and desired opacity level respectively.


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
There are 65 different colors that can be used, the first 14 colors are:
- `0`: White
- `1`: Red
- `2`: Orange
- `3`: Yellow
- `4`: Lime-green
- `5`: Green
- `6`: Green-blue
- `7`: Turquoise
- `8`: Teal
- `9`: Blue
- `10`: Purple
- `11`: Magenta
- `12`: Fuchsia
- `13`: Grey

The next colors follow the same sequence, starting from red, but in lighter shades, see image.

![Available colors in SVV3D](https://github.com/PabloPalaciosAlonso/SphereVectorVisualizer3D/blob/master/screenshots/shot_0.png)


### Extra parameters

-`Sphere opacity`: The opacity of the spheres can be changed by adding a line "# SPHERE OPACITY X", where X is a real number between 0.0 and 1.0. Here, 0.0 indicates a transparent sphere, and 1.0 indicates an opaque sphere. By default, the opacity is 1.0.

The end of a frame is indicated with a `#` symbol.

