# this is interpolate.py
# define a tuple of control points
cpts = (c0, c1, c2, c3)

# define a corresponding tuple of their positions in time
# from 0 to 1, in this case (0, 1/3, 2/3, 1)
x = []
n = len(cpts)
for i in range(n):
    x = x + [float(i) / float(n-1)]

# interpolate between control points to cover [0,1]
# time interval with a much smaller step
nsteps = 200
for i in range(nsteps):
    t = float(i) / float(nsteps - 1)
    c = EvalCubicSpline(t, x, cpts)
    SetView3D(c)
