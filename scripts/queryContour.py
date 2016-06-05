# this is queryContour.py
DeleteAllPlots()
AddPlot("Contour","density")
contAtts = ContourAttributes()
contAtts.contourMethod = contAtts.Value
contAtts.contourValue = (0.3)
SetPlotOptions(contAtts)
DrawPlots()
print Query("MinMax")
val = GetQueryOutputValue()
print val
