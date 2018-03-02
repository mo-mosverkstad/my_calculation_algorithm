def find_method(num, sum,use=None):
    whole_list = ['0','1','2','3','4','5','6','7','8','9', '+','-','*','/','%'] + num if use == None else use+num
    guesses = []
    gnum = 0
    for n1 in whole_list:
        for n2 in whole_list:
            for n3 in whole_list:
                for n4 in whole_list:
                    for n5 in whole_list:
                        try:
                            st = n1+n2+n3+n4+n5
                            thing = eval(st)
                            if thing == sum:
                                guesses.append(st)
                                print('[GUESS '+str(gnum)+']'+st)
                                gnum += 1
                        except:
                            pass
    return guesses

print(find_method(['2','5','99'],-555))
'''

'''