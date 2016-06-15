# this is setControlPoint.py
from math import *
c0 = View3DAttributes()
phi = 0   # 0 <= phi <= 2*pi
theta = 0   # -pi/2 <= theta <= pi/2
c0.viewNormal = (cos(theta)*cos(phi),cos(theta)*sin(phi),sin(theta))
c0.focus = (0, 0, 0)
c0.viewUp = (0, 0, 1)
c0.viewAngle = 30
c0.parallelScale = 17.3205
c0.nearPlane = -34.641
c0.farPlane = 34.641
c0.perspective = 1
SetView3D(c0)
