import re
#
with open('../testdata/14_testdata.dat') as f:
#with open('../data/14_data.dat') as f:
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
            line[O] = "."  # works if we assume the list is from small to large
            if O > B_pos[b_index]:  # We are to the right of current cube
                while O > B_pos[b_index]:  # find next ok block of free space
                    b_index += 1
                ind_block_index = 0  # must be first rolling block
            if b_index == 0:  # moving to the very right 
                line[ind_block_index] = 'O'
            else:
                line[B_pos[b_index-1]+ind_block_index+1] = 'O'
            ind_block_index += 1
        lines_f[k] = line


def cw_rot(lines_f):
    return [list(row) for row in zip(*lines_f[::-1])]

def ccw_rot(lines_f):  # counter clockwise
    return list(zip(*lines_f))[::-1]


def part1():
    lines_f = lines.copy()
    # now uses rotations much cleaner
    lines_f = ccw_rot(lines_f)
    move_right(lines_f)

    res = 0
    for line in lines_f:
        for id, ch in enumerate(line):
            if ch == 'O':
                res += len(line) - id
    print(res)


#part1()




def cycle(lines_f):
    # North
    move_right(lines_f)

    # West
    lines_f = cw_rot(lines_f)
    move_right(lines_f)

    # South
    lines_f = cw_rot(lines_f)
    move_right(lines_f)

    # East
    lines_f = cw_rot(lines_f)
    move_right(lines_f)

    # back to north
    lines_f = cw_rot(lines_f)

    return lines_f



def printit(lines_f):
    for line in lines_f:
        print(line)
    print()

    
# run 3 cycle on the test data for comparing
def part2_test():
    #  copy and make one counter clocwise rotation to bring northe to the left
    lines_f = lines.copy()

    printit(lines_f)
    for kk in range(0,3):
        lines_f = ccw_rot(lines_f)
        lines_f = cycle(lines_f)
        lines_f = cw_rot(lines_f)
        printit(lines_f)


part2_test()






# # res = 0
# # for line in lines_f:
# #     for id, ch in enumerate(line):
# #         if ch == 'X':
# #             res += len(line) - id
# # print(res)




