'''
Usage
python 06-4_notepad.py [src] [dst]
'''

import sys
if (len(sys.argv) > 2) :
    src = sys.argv[1]
    dst = sys.argv[2]
else:
    print("less sys.argv({0})".format(len(sys.argv)))
    exit()

with open(src, 'r') as f:
    data = f.read()

if "\t" in data:
    print("has tap")
else:
    print("T^T")
space_content = data.replace("\t", " "*4)
#print(space_content, "has changed")

with open(dst, 'w') as f:
    f.write(space_content)
