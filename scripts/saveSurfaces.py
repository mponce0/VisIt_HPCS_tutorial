# this is saveSurfaces.py
s = SaveWindowAttributes()
s.format, s.fileName = s.PNG, 'iso'
s.outputToCurrentDirectory = 0
s.outputDirectory = "/Users/razoumov/Documents/teaching/visitWorkshop"
SetSaveWindowAttributes(s)
for i in range(3):
    isoAtts.contourValue = 2. + i*1.5
    SetOperatorOptions(isoAtts)
    name = SaveWindow()
