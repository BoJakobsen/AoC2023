

def cc(x):
    if x=='*':
        isgood = True
    else :
        isgood =False
    return isgood

def ccl(x): #On the line
    if  x=='*':
        isgood = True
    else :
        isgood =False
    return isgood


file = open('data/3_data.dat', 'r')
lines = file.readlines()
file.close()

nums=[]
isgoods=[]
nnum=[ [0]*len(lines[0].strip()) for i in range(len(lines))]
nval=[ [1]*len(lines[0].strip()) for i in range(len(lines))]
ntouched=[ [False]*len(lines[0].strip()) for i in range(len(lines))] # for a given number, indicate if this indet is touched

for index, line in enumerate(lines): #loop the lines
    #print("Line {}: {}".format(index, line.strip()))
    innum=False
    isgood=False
    numstr=''
    for chindex, ch in enumerate(line.strip()) :
        if  ch.isnumeric() : #we are in a number
            numstr += ch
            innum = True

            # check all the nab, not very nice solution
            # Just check the 6 nabs 
            if index>0 and chindex>0 :
                if cc(lines[index-1][chindex-1]) and not ntouched[index-1][chindex-1]:
                    nnum[index-1][chindex-1] += 1
                    ntouched[index-1][chindex-1]=True
                    isgood = True
            
            if index>0  :
                if cc(lines[index-1][chindex]) and not ntouched[index-1][chindex]:
                    isgood = True
                    nnum[index-1][chindex] += 1
                    ntouched[index-1][chindex]=True
            
            if index>0 and (chindex< (len(line.strip())-2) ):
                if cc(lines[index-1][chindex+1])  and not ntouched[index-1][chindex+1]:
                    nnum[index-1][chindex+1] += 1
                    ntouched[index-1][chindex+1]=True
                    isgood = True

            if chindex>0 :
                 if ccl(lines[index][chindex-1]) and not ntouched[index][chindex-1]: 
                    isgood = True
                    nnum[index][chindex-1] += 1
                    ntouched[index][chindex-1]=True

            if chindex>0 and (chindex< (len(line.strip())-2)):
                 if ccl(lines[index][chindex+1]) and not ntouched[index][chindex+1]:
                    nnum[index][chindex+1] += 1
                    ntouched[index][chindex+1]=True
                    isgood = True

            if index<len(lines)-2 and chindex>0 :
                if cc(lines[index+1][chindex-1]) and not ntouched[index+1][chindex-1]:
                    nnum[index+1][chindex-1] += 1
                    ntouched[index+1][chindex-1]=True
                    isgood = True
            
            if index<len(lines)-2 :
                if cc(lines[index+1][chindex]) and not ntouched[index+1][chindex]:
                    nnum[index+1][chindex] += 1
                    ntouched[index+1][chindex]=True
                    isgood = True
            
            if index<len(lines)-2 and (chindex< (len(line.strip())-2) ):
                if cc(lines[index+1][chindex+1]) and not ntouched[index+1][chindex+1] :
                    nnum[index+1][chindex+1] += 1
                    ntouched[index+1][chindex+1]=True
                    isgood = True

        elif (not ch.isnumeric()) and innum  : # a number has ended
            innum = False
            nums.append(int(numstr))
            isgoods.append(isgood)
            for k in range(len(lines)):
                for kk in range(len(line.strip())):
                    if ntouched[k][kk] :
                        nval[k][kk] *= int(numstr)
            numstr=''
            isgood=False
            ntouched=[ [False]*len(lines[0].strip()) for i in range(len(lines))]

    if innum : # line has ended and we are in a number
            nums.append(int(numstr))
            isgoods.append(isgood)
            for k in range(len(lines)):
                for kk in range(len(line.strip())):
                    if ntouched[k][kk] :
                        nval[k][kk] *= int(numstr)
            ntouched=[ [False]*len(lines[0].strip()) for i in range(len(lines))]


print(nnum)
print(nval)

sumit=0
for k in range(len(lines)):
    for kk in range(len(line.strip())):
        if nnum[k][kk]==2 :
            sumit+= nval[k][kk]


print(sumit)