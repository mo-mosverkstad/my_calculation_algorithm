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

def find_average(whole_list):
    sum = 0
    for number in whole_list:
        sum += number
    return float(sum / len(whole_list))

def find_max(the_list):
    max = the_list[0]
    for i in the_list:
        if i > max:
            max = i
    return max

def find_min(the_list):
    min = the_list[0]
    for i in the_list:
        if i < min:
            min = i
    return min

def statistic_list(whole_list):
    d = dict()
    for i in whole_list:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    return d

def find_mode(whole_list):
    Table = statistic_list(whole_list)
    max_value = find_max(list(Table.values()))
    for k,v in Table.items():
        if v == max_value:
            return k

def middle_value(whole_list):
    middle = float(len(whole_list))/2+0.5
    if str(middle)[-1] == '0':
        return whole_list[int(middle)-1]
    elif str(middle)[-1] == '5':
        return (whole_list[int(middle-1.5)]+whole_list[int(middle-0.5)]) / 2

def average_in_statistic_table(d):
    sum = 0
    num = 0
    for k,v in d.items():
        holder = k*v
        num += v
        sum += holder
    return sum/num