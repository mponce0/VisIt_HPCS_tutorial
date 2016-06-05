# this is clipStatic.py
DeleteAllPlots()
AddPlot("Pseudocolor", "density")
c0 = View3DAttributes()
c0.viewNormal = (0.9, 0., 0.4358898943540673)
c0.focus, c0.viewUp = (49.5, 49.5, 49.5), (0, 0, 1)
c0.viewAngle, c0.parallelScale = 30, 85.7365
c0.nearPlane, c0.farPlane, c0.perspective = -171.473, 171.473, 1
SetView3D(c0)

light0 = LightAttributes()
light0.enabledFlag = 1
light0.type = light0.Camera
light0.direction = (0., -0.6, -0.8)
light0.color, light0.brightness = (255, 255, 255, 255), 1
SetLight(0, light0)

AddOperator("Clip")
clipAtts = ClipAttributes()
clipAtts.funcType, clipAtts.plane1Status = clipAtts.Plane, 1
clipAtts.plane1Origin, clipAtts.plane1Normal = (0, 0, 50), (0, 0, 1)
SetOperatorOptions(clipAtts)
DrawPlots()
