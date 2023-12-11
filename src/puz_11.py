
with open('../testdata/11_testdata.dat') as f:
#with open('data/8_data.dat') as f:
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
Nrows=Nch

# find empty lines
for nl in range(Nlines):
    hasgal=False
    for gal in gals.values():
        if gal[0] == nl:
            hasgal=True
    if not hasgal:
        for idx,coor in gals.items():
            if coor[0] > nl:
                print(coor[0])
                gals[idx]=(coor[0]+1,coor[1])
                
                

    


