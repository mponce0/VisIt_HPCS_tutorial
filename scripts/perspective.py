# this is perspective.py
nsteps = 100
a1 = 30
a2 = 60
for i in range(nsteps):
    c0.viewAngle = a1 + float(i)/float(nsteps-1)*(a2-a1)
    SetView3D(c0)
for i in range(nsteps):
    c0.viewAngle = a2 + float(i)/float(nsteps-1)*(a1-a2)
    SetView3D(c0)
