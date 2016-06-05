# this is setControlPoint.py
from math import *
c0 = View3DAttributes()
phi = 0   # 0 <= phi <= 2*pi
theta = 0   # -pi/2 <= theta <= pi/2
c0.viewNormal = (cos(theta)*cos(phi),cos(theta)*sin(phi),sin(theta))
c0.focus = (49.5, 49.5, 49.5)
c0.viewUp = (0, 0, 1)
c0.viewAngle = 30
c0.parallelScale = 85.7365
c0.nearPlane = -171.473
c0.farPlane = 171.473
c0.perspective = 1
SetView3D(c0)
