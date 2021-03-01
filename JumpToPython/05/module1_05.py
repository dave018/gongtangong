# __name__ means file name
def add(a,b):
    print(__name__)
    return a+b
def sub(a,b):
    print(__name__)
    return a-b

# if module1_05.py has some print, it printed in import time
if __name__ == "__main__":
    print(add(1,1))
    print(sub(0,4))