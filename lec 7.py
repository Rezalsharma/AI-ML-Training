import os
with open ("origin.txt","r") as fbsrc, open ("desti.txt","w") as fbst:
    words=fbsrc.read().lower().split(" ")
    for sr in words:
        if sr in ["the","is","of"]:
            fbst.write("are ")
        else:
            fbst.write(sr+" ")
os.remove("origin.txt")
os.rename("desti.txt","origin.txtg")