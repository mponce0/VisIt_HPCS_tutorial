# this is addOperator.py
DeleteAllPlots()
AddPlot("Pseudocolor", "density")
AddOperator("Isosurface")
isoAtts = IsosurfaceAttributes()
isoAtts.contourMethod = isoAtts.Value  # contour by value(s)
isoAtts.variable = "density"
DrawPlots()
print isoAtts   # default is 10 isosurface levels
