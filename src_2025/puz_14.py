import re
#
#with open('../testdata/14_testdata.dat') as f:
with open('../data/14_data.dat') as f:
    lines=[list(x.strip()) for x in f]



def move_right(lines_f):
    for k in range(len(lines_f)):
        line_f_str = "".join(list(lines_f[k]))
        O_pos = [match.start() for match in re.finditer(r'O', line_f_str)]
        B_pos = [match.start() for match in re.finditer(r'#', line_f_str)]

        line = list(lines_f[k])
        B_pos.append(len(line))  # Put a block way to the right fixes edge cases
        b_index = 0
        ind_block_index = 0
        for O in O_pos:
            if O > B_pos[b_index]:  # We are to the right of current cube
                while O > B_pos[b_index]:  # find next ok block of free space
                    b_index += 1
                ind_block_index = 0  # must be first rolling block
            if b_index == 0:  # moving to the very right 
                line[ind_block_index] = 'X'
            else:
                line[B_pos[b_index-1]+ind_block_index+1] = 'X'
            ind_block_index += 1
        lines_f[k] = line


def part1():
    # flip rows and columns for easy movement
    lines_f = list(zip(*lines))
    move_right(lines_f)

    res = 0
    for line in lines_f:
        for id, ch in enumerate(line):
            if ch == 'X':
                res += len(line) - id
    print(res)


part1()



#for line in lines_f:
#    print(line)
#print()

# for line in lines_f:
#     print(line)
# print()
