def middle_value(whole_list):
    middle = float(len(whole_list))/2+0.5
    if str(middle)[-1] == '0':
        return whole_list[int(middle)-1]
    elif str(middle)[-1] == '5':
        return (whole_list[int(middle-1.5)]+whole_list[int(middle-0.5)]) / 2
