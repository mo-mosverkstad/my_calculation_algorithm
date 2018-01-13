import copy

def __comb_iter(contents, comb_list, all_list):
    if len(contents) == 0:
        all_list.append(comb_list)
    else:
        for c in contents:
            new_c = copy.deepcopy(contents)
            new_l = copy.deepcopy(comb_list)
            new_c.remove(c)
            new_l.append(c)
            __comb_iter(new_c, new_l, all_list)

def combinations(contents):
    all_list = []
    __comb_iter(contents, [], all_list)
    return all_list