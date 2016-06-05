# this is queryPseudocolor.py
DeleteAllPlots()
AddPlot("Pseudocolor","density")
DrawPlots()
print Query("MinMax")
val = GetQueryOutputValue()
print val
