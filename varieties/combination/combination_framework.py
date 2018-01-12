import copy

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