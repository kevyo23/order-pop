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

# create_list generates a list of random integers
def create_list(size):
    list = []
    for i in range(size):
        list.append(random.randint(1,20))
    return list

# create_list generates a list of random operations
def create_ops(size):
    sampops = list('*-+')
    olist = []
    for i in range(size - 1):
        olist.append(sampops[i%3])
    return olist


# create_value calculates the result based off the numbers and operations in input lists
def create_value(shuff, ops, size):
    string = ""
    for i in range(size - 1):
        string = string + str(shuff[i]) + ops[i]
    string = string + str(shuff[size - 1])
    return eval(string)

'''
def create_value(shuff, ops, size):
    string = []
    for i in range(size - 1):
        string.append(str(shuff[i]))
        string.append(ops[i])
    string.append(str(shuff[size - 1]))
    return eval(''.join(string))
'''


# main function
def main():
    print "Welcome to order-pop! \n==========================="
    print "Please enter your level of difficulty (3 - 8): "
    # variable initialisation
    try:
        usersize = int(raw_input())
    except ValueError:
        # a non-integer input
        print (Fore.RED + "Please input an integer from 3 - 8 only!")
        print "Reverting to default size 5", Fore.RESET
        usersize = 5
    if usersize < 3 or usersize > 8:
        print (Fore.RED + "Please input an integer from 3 - 8 only!")
        print "Reverting to default size 5", Fore.RESET
        usersize = 5
    win = False
    attempts = 0
    nums = create_list(usersize)
    ops = create_ops(usersize)
    shuff = list(nums)

    # randomise order of numbers and operations
    random.shuffle(shuff)
    random.shuffle(ops)

    # find correct value
    value = create_value(shuff, ops, usersize)

    print "Here are a list of random numbers\n", (Fore.BLUE + ' '.join(map(str, nums))), Fore.RESET
    print "Here are a list of operations, in order\n", (Fore.BLUE + ' '.join(ops)), Fore.RESET
    print "Please enter the numbers in correct order to give", (Fore.BLUE + str(value)), Fore.RESET
    print "Note operation priority i.e. * before + or -\n",

    # determine if user evaluates correct value
    while win != True:
        # max of 10 attempts
        if attempts >= 10:
            print "Game over, correct order is ", ' '.join(map(str, shuff))
            return
        attempts += 1

        if attempts == 8 and usersize > 5:
            print "Here's a hint (first half of the solution) ", ' '.join(map(str,shuff[:(len(shuff)/2)]))

        # user input
        try:
            user = map(int, raw_input().split())
        except ValueError:
            # a non-integer input
            print (Fore.RED + "Please input the correct numbers provided only!"), Fore.RESET
            continue
        if user.__len__() == shuff.__len__():
            # determine user's value
            uservalue = create_value(user, ops, usersize)
        else:
            # more or less numbers input
            print (Fore.RED + str(user.__len__())), "input values detected. Trying to be smart, are we?", Fore.RESET
            continue

        # correct number of integer inputs
        # sort and compare number lists
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
