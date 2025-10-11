import itertools as it
#
#with open('../testdata/12_1_testdata.dat') as f:
with open('../data/12_data.dat') as f:
    lines=[x.strip() for x in f]


# Split the data into the two parts
rec=[]
cgrp=[]
for line in lines:
    tmp=line.split()
    rec.append(tmp[0])
    cgrp.append(list(map(int,tmp[1].split(','))))

# Checkit after filling in right number of '.'
def checkit(rec,cgrp):
    ingrp = False
    cnt = 0
    contgrp_test = []
    for ch in rec:
        if (ch == '#' or ch == '?') and not ingrp:
            ingrp = True
            cnt += 1
        elif (ch == '#' or ch == '?') and ingrp:
            cnt += 1
        elif ch =='.' and ingrp:
            ingrp = False
            contgrp_test.append(cnt)
            cnt = 0
    if ingrp :  # handle end case
            contgrp_test.append(cnt)
    if cgrp == contgrp_test:
        res = True
    else:
        res = False
    return res



# Optimized a bit compared to old solution
#might still be to slow

def prob1() :

    res = 0
    for Nres in range(0,len(rec)):

        # Lets find all numbers we can
        N = len(rec[Nres]) # total springs
        Ndam = sum(cgrp[Nres]) # total damaged springs
        Nop = N-Ndam # Total operational springs

        Nunk = rec[Nres].count('?') # number of unknown springs
        Nop_seen = rec[Nres].count('.') # seen operational springs
        Ndam_seen = rec[Nres].count('#') # seen operational springs

        Nop_toplace = Nop - Nop_seen
        Ndam_toplace = Ndam - Ndam_seen

        IDXunk = [i for i, ltr in enumerate(rec[Nres]) if ltr == '?'] # index for unknowns

        # all ways to place the operational springs
        permut = list(it.combinations(range(Nunk),Nop_toplace))

        for jj in permut:
            Trec = list(rec[Nres])
            for kk in jj:
                Trec[IDXunk[kk]] = '.'
                # all operational is now in, so left over ? is broken
            if checkit(Trec,cgrp[Nres]):
                res += 1

    print(res)

prob1()
