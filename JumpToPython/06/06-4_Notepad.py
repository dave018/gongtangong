'''
Usage
python 06-4_notepad.py [options] ["text"]

#this notepad always uses ./06-4_Notepad.txt

Options
-v : jurt print path
-a : append text. text must be packaged with ""
'''

import sys
if (len(sys.argv) > 1) :
    option = sys.argv[1]
    if (option == '-a' and len(sys.argv)>2) :
        memo = sys.argv[2]
else:
    print("less sys.argv({0})".format(len(sys.argv)))
    exit()

if option == '-a':
    with open("06-4_Notepad.txt", 'a') as f:
        f.write(memo + "\n")
elif option == '-v':
    with open("06-4_Notepad.txt", 'r') as f:
        data = f.read()
        print(data)
else:
    print("[Error] BadOptions")

