from frequency_table import all_list
from find_max import find_max

def find_mode(whole_list):
    Table = all_list(whole_list)
    max_value = find_max(list(Table.values()))
    for k,v in Table.items():
        if v == max_value:
            return k
