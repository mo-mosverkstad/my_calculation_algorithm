def find_min(the_list):
    min = the_list[0]
    for i in the_list:
        if i < min:
            min = i
    return min