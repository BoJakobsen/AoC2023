with open('1/1_1_data.dat') as f:
    sumit=0
    for line in f:
        linenum=[]
        for ch in line:
            #print(ch)
            if ch.isnumeric():
                linenum.append(int(ch))
        sumit+= (linenum[0]*10 + linenum[-1])
print(sumit)


