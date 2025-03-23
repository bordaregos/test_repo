# test code
import random


def lst_calc(values):
    res_lst = [random.randrange(1, 10) for _ in range(values)]
    print(res_lst)


lst_calc(int(input(f'Enter number: ')))
