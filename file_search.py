import os
def search(name, path='.', ld=[]):
    for x in os.listdir(path):
        print x
        y=os.path.join(path,x)
        print y
        if os.path.isdir(y):
            search(name,y,ld)
        elif os.path.isfile(y) and x.find(name)!=-1:
            print y
            ld.append(y)
        return ld

file = search('c')
print file
