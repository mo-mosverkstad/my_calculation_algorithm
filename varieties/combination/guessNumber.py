from combination_framework import combinations

def guessNumber(numbers, operaters, target):
    pass_list = []
    for num in combinations(numbers):
        for op in combinations(operaters):
            calc = '((' + num[0] + op[0] + num[1] + ')' + op[1] + num[2] + ')' + op[2] + num[3]
            if float(eval(calc)) == float(target):
                pass_list.append(f'{calc} = {target}')
    return pass_list