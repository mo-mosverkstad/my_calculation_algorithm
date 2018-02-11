from find_max import find_max
def mode_in_freq_table(Table):
    max_value = find_max(list(Table.values()))
    for k,v in Table.items():
        if v == max_value:
            return k
