import os
def walk(dirname):
    for name in os.listdir(dirname):
        path=os.path.join(dirname,name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
dirname='/home/linux/pramod/think'
walk(dirname)
