#!/usr/bin/env python

'''

order-pop:
A simple Python game where users reorder given numbers to find the correct result.
Operations locations are fixed - users fit the given numbers around the operations
Written by Kevin Yu on 24/12/2016

'''

import random
from colorama import init, Fore
init()

def create_list():
    list = []
    for i in range(4):
        list.append(random.randint(1,10))
    return list

def create_value(shuff, ops):
    return eval(str(shuff[0]) + ops[0] + str(shuff[1]) + ops[1] + str(shuff[2]) + ops[2] + str(shuff[3]))

def main():
    win = False
    attempts = 0
    nums = create_list()
    shuff = list(nums)
    ops = list('+-*')

    random.shuffle(shuff)
    random.shuffle(ops)
    value = create_value(shuff, ops)

    print "Welcome to order-pop! \n===========================\n",
    print "Here are a list of random numbers\n", (Fore.BLUE + ' '.join(map(str, nums))), Fore.RESET
    print "Here are a list of operations, in order\n", (Fore.BLUE + ' '.join(ops)), Fore.RESET
    print "Please enter the numbers in correct order to give", (Fore.BLUE + str(value)), Fore.RESET
    print "Note operation priority i.e. * before + or -\n",

    while win != True:
        if attempts > 10:
            print "Game over, correct order is ", ' '.join(map(str, shuff))
            return
        attempts += 1
        try:
            user = map(int, raw_input().split())
        except ValueError:
            print (Fore.RED + "Please input the correct numbers provided only!"), Fore.RESET
            continue
        if user.__len__() == shuff.__len__():
            uservalue = create_value(user,ops)
        else:
            print (Fore.RED + str(user.__len__())), "input values detected. Trying to be smart, are we?", Fore.RESET
            continue
        shuff.sort()
        user.sort()
        if shuff == user:
            if uservalue == value:
                print "===========================\nWell done, that is correct!"
                win = True;
            else:
                print (Fore.RED + "Incorrect, your order gives"), uservalue, Fore.RESET
        else:
            print (Fore.RED + "Incorrect input detected. Please use values provided."), Fore.RESET
main()
