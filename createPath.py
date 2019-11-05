import os

def checkPath(path):
    if not os.path.exists(str(path)):
        return False
    else:
        return True
def createPath(path):
    if not checkPath(path):
        try:
            os.makedirs(str(path))
        except OSError as e:
            print("Error Creating ",str(path),": [ %s ]"% e)

def deletePath(path):
    if checkPath(path):
        try:
            os.rmdir(str(path))
        except OSError as e:
            print("Error Creating ",str(path),": [ %s ]"% e)

def createFile(path,filename,content):
    path = str(path)
    if not checkPath(path):
        createPath(path)
    try:
        with open(path+"/"+filename, "w+") as f:
            f.write(content)
            # os.utime(path, None)
    except OSError as e:
        print("Error Creating ",str(path),": [ %s ]"% e)

def listDirectory(path):
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            print(directory)

# # Examples of Usage
# createPath(12345)
# listDirectory("/mnt/d/FYP")
# deletePath(1234)
# deletePath(12345)