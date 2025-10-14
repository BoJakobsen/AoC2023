#with open('../testdata/13_testdata.dat') as f:
with open('../data/13_data.dat') as f:
    a = f.read().strip()
    maps = a.split('\n\n')  # Split on empty line


def findit(mapl):
    for k in range(1, len(mapl)):
        u = k-1
        d = k
        found = True
        while u >= 0 and d < len(mapl):
            # print(u,d,mapl[u],mapl[d])
            if mapl[u] != mapl[d]:
                found = False
                break
            else:
                u -= 1
                d += 1
        if found:
            # print(k, found)
            return k
    return 0

def part1():
    res = 0
    for map0 in maps:

        # convert to list of lists
        mapl = list(map(list, map0.split('\n')))

        # rotated 90 deg
        maplr = list(zip(*mapl))

        res += 100 * findit(mapl)
        res += (findit(maplr))
    print(res)

part1()
    
# print map and rotated map
# for l in mapl:
#     print("".join(l))

# print("")
    
# for l in maplr:
#     print("".join(l))
    
