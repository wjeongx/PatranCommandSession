import os
import sys
from PatranCommandSession import p3Utilities as UTL

nastranbdf = UTL.FileOpenLoad()

f = open(nastranbdf, 'r')
fw = open('loads.bdf', 'w')

ext_path = os.path.abspath(nastranbdf)

print(ext_path)

'''
while True:
    xline = f.readline()
    if xline[0] == '$':
       fw.write(xline) 
'''    
f.close()
fw.close()