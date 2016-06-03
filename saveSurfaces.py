# this is saveSurfaces.py
s = SaveWindowAttributes()
s.format = s.PNG
s.progressive = 0
for i in range(3):
   isoAtts.contourValue = 0.6 + i*0.4
   SetOperatorOptions(isoAtts)
   s.fileName = '/Users/razoumov/Desktop/iso'+str(i)
   print s.fileName
   SetSaveWindowAttributes(s)
   name = SaveWindow()
