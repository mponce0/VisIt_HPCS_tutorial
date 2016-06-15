# this is addOperator.py
DeleteAllPlots()
AddPlot("Pseudocolor", "hardyglobal")
AddOperator("Isosurface")
isoAtts = IsosurfaceAttributes()
isoAtts.contourMethod = isoAtts.Value  # contour by value(s)
isoAtts.variable = "hardyglobal"
DrawPlots()
print isoAtts   # default is 10 isosurface levels
