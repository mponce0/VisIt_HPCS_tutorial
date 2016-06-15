# this is flyInOut.py
nsteps = 100
xfirst = 0
xlast = -30
for i in range(nsteps):
    x = xfirst + float(i)/float(nsteps-1)*(xlast-xfirst)
    c0.focus = (x, 0, 0)
    SetView3D(c0)
for i in range(nsteps):
    x = xlast + float(i)/float(nsteps-1)*(xfirst-xlast)
    c0.focus = (x, 0, 0)
    SetView3D(c0)
