from setuptools import setup, find_packages

setup(
    name='SVV3D',
    version='1.0',
    packages=find_packages(),
    author='P. Palacios-Alonso',
    author_email='pablo.palaciosa@uam.es',
    description='App to visualize animations that contain spheres and arrows',
    install_requires=[
        'pynput',
        'vpython',
        'argparse'
        # Lista de dependencias requeridas por tu aplicación
    ],

    entry_points={
        'console_scripts': [
            'SVV3D = SVV3D.SVV3D:main',
        ],
    }
)
