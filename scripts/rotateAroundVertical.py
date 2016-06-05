# this is rotateAroundVertical.py
nsteps = 300
for i in range(nsteps):
    phi = float(i)/float(nsteps-1)*2.*pi
    c0.viewNormal = (cos(theta)*cos(phi), cos(theta)*sin(phi),
                     sin(theta))
    SetView3D(c0)
