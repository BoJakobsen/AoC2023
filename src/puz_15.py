

def HASH(string):
    val=0
    for ch in string:
        val += ord(ch)
        val *=17
        val = val % 256
    return val
    
def part1():
    # as input is one long line, read one char at the time
    #with open('testdata/15_testdata.dat') as f:
    with open('data/15_data.dat') as f:
        sumit=0    
        while True:
            string=''
            ch=f.read(1)        
            if not ch:
                break
            while (ch !=',')  and (ch !='\n'):
                string+= ch
                ch=f.read(1)
                if not ch:
                    break
            HASHVal= HASH(string)
            sumit+=HASHVal
            print(string,HASHVal)
    print(sumit)

part1()