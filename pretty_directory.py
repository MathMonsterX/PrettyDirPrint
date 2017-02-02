import os

def isDir(dirobj):
    return os.path.isdir(dirobj)

def recSearchDir(depth,directory):
    depthTab = ""
    for x in range(0, depth):
        depthTab += "  "

    dirnames = []
    filenames = []
    for name in os.listdir(directory):
        if isDir(directory+'/'+name):
            dirnames.append(name)
        else:
            filenames.append(name)

    if directory != '.':
        print("{}{}".format(depthTab, os.path.dirname(directory)))
    
    if '.git' in dirnames:
        dirnames.remove('.git')
            
    for subdirname in dirnames:
        recSearchDir(depth+1, directory+"/"+subdirname)

    for filename in filenames:
        print("{}  - {}".format(depthTab, filename))

        
    
def main():
    recSearchDir(0, '.')

if __name__ == "__main__":
    main()
