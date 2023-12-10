#with open('testdata/5_testdata.dat') as f:
with open('data/8_data.dat') as f:
    lines=[x.strip() for x in f]

inst=lines[0].strip()
inst=[0 if x=='L' else 1  for x in lines[0]]


map={}
for kk in range(2,len(lines)):
    lab,node = lines[kk].split('=')   
    node = ((node.replace('(',' ')).replace(')',' ')).strip()
    node0,node1=node.split(',')
    map[lab.strip()] = (node0.strip(),node1.strip())


steps=0
lab='AAA'
kk=0
while lab != 'ZZZ':
    node=map[lab]
    lab=node[inst[kk]]
    kk+=1
    if kk == len(inst):
        kk=0
    steps += 1

print(steps)

