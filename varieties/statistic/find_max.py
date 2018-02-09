def find_max(the_list):
    max = the_list[0]
    for i in the_list:
        if i > max:
            max = i
    return max