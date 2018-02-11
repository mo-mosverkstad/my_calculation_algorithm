from middle_value import middle_value

def middle_value_in_frequncy_table(ft): # ft means frequncy table
    result = list()
    for x, f in ft.items():
        for v in range(f):
            result.append(x)
    return middle_value(result)

