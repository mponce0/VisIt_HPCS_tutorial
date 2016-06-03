# this is oneSurface.py
DeleteAllPlots()
AddPlot('Contour', 'density')
contAtt = ContourAttributes()
contAtt.contourMethod = contAtt.Value
contAtt.contourValue = (0.3)
contAtt.colorType = contAtt.ColorBySingleColor
contAtt.singleColor = (0, 255, 0, 255)
SetPlotOptions(contAtt)
DrawPlots()
