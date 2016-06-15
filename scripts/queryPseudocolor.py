# this is queryPseudocolor.py
DeleteAllPlots()
AddPlot("Pseudocolor","hardyglobal")
DrawPlots()
print Query("MinMax")
val = GetQueryOutputValue()
print val
