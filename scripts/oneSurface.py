# this is oneSurface.py
DeleteAllPlots()
AddPlot('Contour', 'hardyglobal')
contAtt = ContourAttributes()
contAtt.contourMethod = contAtt.Value
contAtt.contourValue = (3.8)
contAtt.colorType = contAtt.ColorBySingleColor
contAtt.singleColor = (0, 255, 0, 255)
SetPlotOptions(contAtt)
DrawPlots()
