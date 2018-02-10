def average_in_statistic_table(d):
    sum = 0
    num = 0
    for k,v in d.items():
        holder = k*v
        num += v
        sum += holder
    return sum/num
