def if_func(condition, do, else_do='pass'):
    if condition:
        exec(do)
    else:
        exec(else_do)

def loop_at(this_list, do_what, varible_nm):
    exec(f'for {varible_nm} in this_list:')
    exec(f'    '+do_what)

