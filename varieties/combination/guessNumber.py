from combination_framework import combinations

def guessNumber(numbers, target):
    operaters = ['+', '-','*', '/']
    all_op_comb = []
    all_num_comb = []
    combinations(operaters, [], all_op_comb)
    combinations(numbers, [], all_num_comb)
    pass_num = 0
    for num in all_num_comb:
        for op in all_op_comb:
            calc = '((' + num[0] + op[0] + num[1] + ')' + op[1] + num[2] + ')' + op[2] + num[3]
            if float(eval(calc)) == float(target):
                print(f'{calc} = {target}')
                pass_num += 1
    print(f'Total number of solution which can reach {target}: {pass_num}')

guessNumber(['1','2','5','7'], 24)