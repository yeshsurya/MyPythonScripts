import os
from os import listdir
from os.path import  isfile,join
import shutil
# print(os.path.join(os.environ['HOMEPATH'])+"\Desktop")
filePath = os.path.join(os.environ['HOMEPATH'])+"\Desktop"
# print(os.W_OK)

# Check if path is accessible

# print(os.access(filePath,os.W_OK))
extnList=[]
if(os.access(filePath,os.W_OK)):
    #list all files found in this path
    onlyfiles = [f for f in listdir(filePath) if isfile(join(filePath, f))]
    for ele in onlyfiles:
        # print(ele.split(".")[1])
        if(extnList.__contains__(ele.split(".")[-1])):
            continue
        else:
            extnList.append(ele.split(".")[-1])
for ele in extnList:
    print(filePath+"\\"+"DeskStack\\"+ele)
    try:
        os.stat(filePath+"\\"+"DeskStack\\"+ele)
    except:
        os.mkdir(filePath+"\\"+"DeskStack\\"+ele)
test = listdir(filePath)
print("____________Movement begins ___________")
for ele in test:
    # print(join(filePath,ele))
    #print(filePath+"\\"+"DeskStack\\"+ele.split(".")[-1])
    try:
        shutil.move(join(filePath,ele),filePath+"\\"+"DeskStack\\"+ele.split(".")[-1])
        print("Moving "+ele+" to "+filePath+"\\"+"DeskStack\\"+ele.split(".")[-1])
    except:
        continue
    # print(ele.split(".")[-1])