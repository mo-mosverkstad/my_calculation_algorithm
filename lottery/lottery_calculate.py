from random import randint

tries = 10000

profit = 0
cost   = 0
get_win_num = 1
for i in range(tries):
    randomnumber = randint(1,12)
    get_win_num = randint(1,12)
    print(str(i) + ': number : ' + str(get_win_num) + ', spin result : ' + str(randomnumber))
    if get_win_num == randomnumber:
        profit += 20
    cost +=5

print('I got '+str(profit)+' after spending ' + str(cost))
print('Profit '+str(profit/tries))