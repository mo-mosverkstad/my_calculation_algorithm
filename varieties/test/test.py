import os, sys, inspect

def add_path():
    # realpath() will make your script run, even if you symlink it :)
    cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
    if cmd_folder not in sys.path: sys.path.insert(0, cmd_folder)

def add_path_subfolder(subfolder):
    # Use this if you want to include modules from a subfolder
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0], subfolder)))
    if cmd_subfolder not in sys.path: sys.path.insert(0, cmd_subfolder)

def verify_testcases(testcases):
    pass_number = 0
    total_number = len(testcases)
    for name, tc in testcases.items():
        func, args, expect = tc
        if func(*args) == expect: pass_number += 1
        else: print(f'Error: {name} is wrong')
    print(f'Pass rate is {pass_number / total_number * 100}% ({pass_number} out of {total_number})')


add_path()
add_path_subfolder('..\\combination')
add_path_subfolder('..\\statistic')

from guessNumber import guessNumber
from find_min import find_min
from find_max import find_max
from find_average import find_average
from middle_value import middle_value

testcases = {'TC_GUESS24_01': (guessNumber, 
                               (['1','2','5','7'], ['+', '-','*', '/'], 24), 
                               ['((5/1)+7)*2 = 24', '((5+7)/1)*2 = 24', '((5+7)*2)/1 = 24', '((7/1)+5)*2 = 24', '((7+5)/1)*2 = 24', '((7+5)*2)/1 = 24']),
             'TC_GUESS21_02': (guessNumber,
                               (['1','5','8','7'], ['+', '-', '*', '/'], 21),
                               ['((8/1)-5)*7 = 21', '((8-5)/1)*7 = 21', '((8-5)*7)/1 = 21']),
             'TC_FIND_MIN_01':(find_min,
                               ([8,3,4,5,33,999,-2],),
                               -2),
             'TC_FIND_MAX_01':(find_max,
                               ([88,23,7373,3883,3939,3,93,93,939343,3993,38],),
                               939343),
             'TC_FIND_AVERAGE':(find_average,
                                ([1,2,3,4,8],),
                                3.6),
             'TC_MIDDLE_VALUE':(middle_value,
                                ([1,2,3,4,8],),
                                3)}



verify_testcases(testcases)