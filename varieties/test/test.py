import sys
sys.path.append('..\combination')

from guessNumber import guessNumber

testcases = {'TC_GUESS24_01': (guessNumber, 
                               (['1','2','5','7'], ['+', '-','*', '/'], 24), 
                               ['((5/1)+7)*2 = 24', '((5+7)/1)*2 = 24', '((5+7)*2)/1 = 24', '((7/1)+5)*2 = 24', '((7+5)/1)*2 = 24', '((7+5)*2)/1 = 24']),
             'TC_GUESS21_02': (guessNumber,
                               (['1','5','8','7'], ['+', '-', '*', '/'], 21),
                               ['((8/1)-5)*7 = 21', '((8-5)/1)*7 = 21', '((8-5)*7)/1 = 21']),
             }

def verify_testcases(testcases):
    pass_number = 0
    total_number = len(testcases)
    for name, tc in testcases.items():
        func, args, expect = tc
        if func(*args) == expect: pass_number += 1
        else: print(f'Error: {name} is wrong')
    print(f'Pass rate is {pass_number / total_number * 100}% ({pass_number} out of {total_number})')

verify_testcases(testcases)