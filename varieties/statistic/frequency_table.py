def all_list(whole_list):
    d = dict()
    for i in whole_list:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    return d

print(all_list([1,1,2,2,2,1,2,1,2,1,2]))