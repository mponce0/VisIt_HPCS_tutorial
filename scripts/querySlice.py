# this is querySlice.py
DeleteAllPlots()
AddPlot("Pseudocolor", "hardyglobal")
AddOperator("Slice")
DrawPlots()
for i in range(10):
    position = i*2 - 9
    print position
    s = SliceAttributes()
    s.axisType = s.XAxis
    s.originType = s.Intercept
    s.originIntercept = position
    SetOperatorOptions(s)
    Query("MinMax")   # queries the 3D volume!
    print 'minMax =', GetQueryOutputValue()
    Query("Weighted Variable Sum")   # queries the 2D slice!
    print 'sum =', GetQueryOutputValue()
