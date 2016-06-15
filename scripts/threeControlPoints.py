# this is threeControlPoints.py
c1 = View3DAttributes()
copyView(c0,c1)
phi = pi/2
c1.viewNormal = (cos(theta)*cos(phi), cos(theta)*sin(phi),
                 sin(theta))

c2 = View3DAttributes()
copyView(c1,c2)
theta = pi/6
c2.viewNormal = (cos(theta)*cos(phi), cos(theta)*sin(phi),
                 sin(theta))

c3 = View3DAttributes()
copyView(c2,c3)
c3.focus = (0, -30, -20)
