from calculation_framework import *
from another_framework import *

status = 'root'
COMMAND_BACK = 'back'
COMMAND_CAL = 'calculate'
COMMAND_HELP = 'help'
COMMAND_EXIT = 'exit'
COMMAND_BIF = 'built_in features'
COMMAND_CBF = 'code features'
o = {'/c':'combinations', 'avg':'find_average', '^': 'find_max', 'v':'find_min', 'sList': 'statistic_list', 'md': 'find_mode', '//':'middle_value'
     ,'avg*': 'average_in_statistic_table', '//*': 'middle_value_in_frequncy_table', 'md*':'mode_in_freq_table', ':~': 'time_change'
     ,'<>':'if_func',';':'loop_at'}

print('Type help if you don\'t know how to use this calculator \ntype exit to get out')
while True:
    command = input(':>')
    if status == 'root':
        if command == COMMAND_CAL:
            inputs = input('.....')
            howto = input('.....')
            if inputs.startswith('Input digits'):
                inputs = eval('['+inputs[12:]+']')
                for k, v in o.items():
                    howto = howto.replace(k,v)
                print(eval(howto))
            else:
                print('N/A')
        elif command == COMMAND_EXIT:
            break
        elif command == 'help':
            print('First type calculate')
            print('Then you will see "....."\nYou had to type first "Input digits"\nAfter that you type what you want to do in abstract mode')
            print('Then you will press enter and you will get answer\nIf you got "N/A" you had write wrong')
            print('This calculator has some built-in features +, -, *, /, /c that means combinations, avg that means average, ^ means find_max, v means find_min')
            print('sList means that you generate your own statistic list, md means mode, // means middle_value, avg* means you find average in ')
            print('statistic list, //* means you find mode in statistic list, md* means mode in statistic list, :~ means time change')
            print('Important: you have to put a tuple behind the keyword, for example "/c"(You don\'t have to put a tuple behind +,-,*,/)')
            print(f'See more when you type {COMMAND_BIF} and {COMMAND_CBF}')
            print('If you want to exit press exit')
        elif command == COMMAND_BIF:
            print('+,-,*,/,/c,avg,^,v,sList,md,//,avg*,//*,md*,:~')
        elif command == COMMAND_CBF:
            print('<>:if,;:for loop at')
        