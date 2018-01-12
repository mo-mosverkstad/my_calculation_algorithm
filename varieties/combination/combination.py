import copy

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def combinations(contents, comb_list, all_list):
    if len(contents) == 0:
        all_list.append(comb_list)
    else:
        for c in contents:
            new_c = copy.deepcopy(contents)
            new_l = copy.deepcopy(comb_list)
            new_c.remove(c)
            new_l.append(c)
            combinations(new_c, new_l, all_list)

all_list = []
combinations([1,2,3,4,5], [], all_list)
for i in range(len(all_list)): print('%4d, %s'%(i, str(all_list[i])))
print('---- total number: %d ----'%(len(all_list)))
