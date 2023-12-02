
with open('2_data.dat') as f:
    sumit=0
    kk=1
    for line in f:
        possible=True
        dat1=line[0:-1].split(':')[1]
        hands=dat1.split(';')
        for hand in hands:
            collors=hand.split(',')
            #print(collors)
            for collor in collors:
                dat=collor.split(' ')
                #print(dat[2])
                #print(dat[1])
                if dat[2]=='red' and int(dat[1])>12:
                     possible=False
                if dat[2]=='green' and int(dat[1])>13:
                     possible=False
                if dat[2]=='blue' and int(dat[1])>14:
                     possible=False
        print(kk)
        print(possible)
        if possible:
            sumit += kk
        kk+=1
print(sumit)



                
            #print(collors[1].split(' '))
        #print(val[idx.index(min(idx))])
        #print(val[idx.index(max(idx))])
        #sumit+= (val[idx.index(min(idx))]*10 + val2[idx2.index(max(idx2))])
        #print(sumit)


