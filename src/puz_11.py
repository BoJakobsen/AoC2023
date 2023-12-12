
from copy import deepcopy
import numpy as np

#with open('../testdata/11_testdata.dat') as f:
with open('data/11_data.dat') as f:
    lines=[x.strip() for x in f]

# make map of galaxies
gals={}
Ngal=0
Nline=0
for line in lines:
    Nch=0
    for ch in line:
        if ch=='#':
            gals[Ngal]=(Nline,Nch)
            Ngal +=1
        Nch+=1
    Nline+=1
Nlines=Nline
Ncolu=Nch

new_gals=deepcopy(gals)

# find empty lines
for nl in range(Nlines):
    hasgal=False
    for gal in gals.values():
        if gal[0] == nl:
            hasgal=True
    if not hasgal: # move down
        for key,coor in gals.items() :
            if coor[0]>nl:
                new_gals[key]=(new_gals[key][0]+1,new_gals[key][1])

# find empty rows
for nc in range(Ncolu):
    hasgal=False
    for gal in gals.values():
        if gal[1] == nc:
            hasgal=True
    if not hasgal: # move down
        print('nc', nc)
        for key,coor in gals.items() :
            if coor[1]>nc:
                print(key, coor)
                new_gals[key]=(new_gals[key][0],new_gals[key][1]+1)
      
  
# we have now expanded the universe
gals=new_gals    

def dist(x0,x1):
    res=np.sqrt((x0[0]-x1[0])**2+(x0[1]-x1[1])**2)
    return res


sumdist=0
# loop over all pairs
for k in range(len(gals)):
    for kk in range(k+1,len(gals)):
        # now finde distance
        #print(k,kk)
        Ndist=0
        AtGoal=False
        x1=gals[k]
        y=gals[kk]
        while not AtGoal : 
            # u d l r
            chan=[dist((x1[0]-1,x1[1]),y), dist((x1[0]+1,x1[1]),y), dist((x1[0],x1[1]-1),y) , dist((x1[0],x1[1]+1),y)]
            nn=np.argmin(chan)
            if nn==0:
                x1=(x1[0]-1,x1[1])
            elif nn==1:
                x1=(x1[0]+1,x1[1])
            elif nn==2:
                x1=(x1[0],x1[1]-1)
            elif nn==3:
                x1=(x1[0],x1[1]+1)
            if x1[0]==y[0] and x1[1]==y[1]:
                AtGoal=True
            Ndist+=1
        #print(Ndist)
        sumdist+= Ndist

print(sumdist)





        





