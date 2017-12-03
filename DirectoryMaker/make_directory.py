import os
fh=open("Lecture List.txt","r")
tst=os.getcwd()
for ele in fh.readlines():
    pat=tst+"\\"+ele
    pat=pat.replace("\n","")
    pat=pat.replace("""\\""",""">""")


    if(os.path.exists(pat.replace(">","\\"))):
        pass
    else:
        os.mkdir(pat.replace(">","\\"))
        print(pat.replace(">","\\"))
