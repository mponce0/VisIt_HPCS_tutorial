# this is flyInOut.py
nsteps = 100
xfirst = 49.5
xlast = -175
for i in range(nsteps):
    x = xfirst + float(i)/float(nsteps-1)*(xlast-xfirst)
    c0.focus = (x, 49.5, 49.5)
    SetView3D(c0)
for i in range(nsteps):
    x = xlast + float(i)/float(nsteps-1)*(xfirst-xlast)
    c0.focus = (x, 49.5, 49.5)
    SetView3D(c0)
