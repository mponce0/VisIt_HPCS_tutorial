# this is queryContour.py
DeleteAllPlots()
AddPlot("Contour","hardyglobal")
contAtts = ContourAttributes()
contAtts.contourMethod = contAtts.Value
contAtts.contourValue = (3.8)
SetPlotOptions(contAtts)
DrawPlots()
print Query("MinMax")
val = GetQueryOutputValue()
print val
