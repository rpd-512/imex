from PIL import Image
import sys
from os import path
pth = (sys.argv[1])
img = Image.open(pth)

img = img.resize((int(200),int(100*(img.size[1]/img.size[0]))))

pix = img.load()
tran = 0
if(img.mode == "RGBA"):
    tran = 1
totT = ""
for y in range(img.size[1]):
    for x in range(img.size[0]):
        p = pix[x,y]
        if(p==(0,0,0)):
            c=" "
        elif(tran == 1 and p[3]==0):
            c=" "
        elif(p==(255,255,255)):
            c="e"
        elif(p[0]>100 and p[0]<300 and p[1]>100 and p[1]<200 and p[2]>50 and p[2]<150):
            c="X"
        elif(p[0]>10 and p[0]<125 and p[1]>0 and p[1]<40 and p[2]>0 and p[2]<36):
            c="#"
        elif(p[0] > p[1] or p[0] > p[2] and p[0] > 100):
            c="0"
        elif(p[1] > p[0] or p[1] > p[2] and p[1] > 100):
            c="1"
        elif(p[2] > p[1] or p[2] > p[0] and p[2] > 100):
            c="2"
        elif(p[0] < 75 and p[1]<75 and p[2]<75):
            c="W"
        else:
            c="O"
        totT+=c
    totT+="\n"
name = path.splitext(path.basename(pth))
name = (name[0]+"_imex.txt")
print(totT)
with open(name,"w") as f:
    f.write(totT)
