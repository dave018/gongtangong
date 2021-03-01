import os

def search(dirname):
    try:
        filenames = os.listdir(dirname) #return "dir" result.
        for filename in filenames:
            full_filename = os.path.join(dirname, filename) #not str.join(). this join is for path + subpath
            if os.path.isdir(full_filename):
                search(full_filename)
            ext = os.path.splitext(full_filename)[-1] #splitext return (others, .py)
            if ext == '.py':
                print(full_filename)
    except PermissionError:
        pass

search(os.getcwd())

print("="*20)

#like below codes, os.walk() return every sub path with dir[] and files[]
for(path, dir, files) in os.walk(os.getcwd()):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" %(path, filename))

