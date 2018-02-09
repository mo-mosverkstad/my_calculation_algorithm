def find_average(whole_list):
    sum = 0
    for number in whole_list:
        sum += number
    return float(sum / len(whole_list))