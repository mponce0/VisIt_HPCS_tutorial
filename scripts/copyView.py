# this is copyView.py
def copyView(a,b):
    b.viewNormal = a.viewNormal
    b.focus = a.focus
    b.viewUp = a.viewUp
    b.viewAngle = a.viewAngle
    b.parallelScale = a.parallelScale
    b.nearPlane = a.nearPlane
    b.farPlane = a.farPlane
    b.perspective = a.perspective
