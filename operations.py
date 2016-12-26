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
def create_list(size, mode):
    if mode == "E":
        selectfrom = 10
    elif mode == "H":
        selectfrom = 40
    else: # mode == "N"
        selectfrom = 20
    list = []
    for i in range(size):
        list.append(random.randint(1,selectfrom))
    return list

# create_list generates a list of random operations
def create_ops(size, mode):
    if mode == "E":
        sampops = ('+-+')
    else: # mode == "N" or mode == "H"
        sampops = ('*-+')
    olist = []
    for i in range(size - 1):
        olist.append(sampops[i%3])
    return olist


# create_value calculates the result based off the numbers and operations in input lists
def create_value(list, olist, size, user):
    string = ""
    for i in range(size - 1):
        string = string + str(list[i]) + olist[i]
    string = string + str(list[size - 1])
    if user:
        print string
    return eval(string)

'''
# alternative method of above function
def create_value(list, olist, size):
    string = []
    for i in range(size - 1):
        string.append(str(list[i]))
        string.append(olist[i])
    string.append(str(list[size - 1]))
    return eval(''.join(string))
'''

def run_attempt(list, olist, usersize, cvalue):
    # user input
    try:
        user = map(int, raw_input().split())
    except ValueError:
        # a non-integer input
        print (Fore.RED + "Please input the correct numbers provided only!"), Fore.RESET
        return False
    if user.__len__() == list.__len__():
        # determine user's value
        uservalue = create_value(user, olist, usersize, 1)
    else:
        # more or less numbers input
        print (Fore.RED + str(user.__len__())), "input values detected. Trying to be smart, are we?", Fore.RESET
        return False

    # correct number of integer inputs
    # sort and compare number lists
    list.sort()
    user.sort()
    if list == user:
        if uservalue == cvalue:
            print "===========================\nWell done, that is correct!"
            return True;
        else:
            print (Fore.RED + "Incorrect, your order gives"), uservalue, Fore.RESET
    else:
        print (Fore.RED + "Incorrect input detected. Please use values provided."), Fore.RESET
    return False


# main function
def main():
    level_all = list(range(3, 9))
    level_win = []
    end = False
    print "Welcome to order-pop! \n==========================="
    usermode = raw_input("Please enter your play mode i.e. Easy, Normal, Hard (E, N, H): ")
    if usermode != "E" and usermode != "N" and usermode != "H":
        print (Fore.RED + "Please input E, N or H only!")
        print "Reverting to default mode Normal", Fore.RESET
        usermode = "N"

    while not end:
        print "Level status:",(Fore.GREEN + ' '.join(map(str, level_win))),(Fore.BLUE + ' '.join(map(str, level_all))), Fore.RESET
        print "Loading level ", (Fore.BLUE + str(level_all[0])), Fore.RESET
        usersize = level_all[0]
        # variable initialisation
        win = False
        attempts = 0
        nums = create_list(usersize, usermode)
        ops = create_ops(usersize, usermode)
        shuff = list(nums)

        # randomise order of numbers and operations
        random.shuffle(shuff)
        random.shuffle(ops)

        # find correct value
        value = create_value(shuff, ops, usersize, 0)

        print "Here are a list of random numbers\n", (Fore.BLUE + ' '.join(map(str, nums))), Fore.RESET
        print "Here are a list of operations, in order\n", (Fore.BLUE + ' '.join(ops)), Fore.RESET
        print "Please enter the numbers in correct order to give", (Fore.BLUE + str(value)), Fore.RESET
        print "Note operation priority i.e. * before + or -\n",

        # determine if user evaluates correct value
        while not win:
            # max of 10 attempts
            if attempts >= 10:
                print "Game over, correct order is ", ' '.join(map(str, shuff))
                break
            attempts += 1

            if attempts == 8:
                print "Here's a hint (first section of the solution) ", ' '.join(map(str,shuff[:(len(shuff)/2)]))
            win = run_attempt(shuff, ops, usersize, value)

        if win:
            level_win.append(usersize)
            level_all.remove(usersize)
            if usersize == 8:
                print (Fore.GREEN + "Congratulations! You have beaten all levels. Thank you for playing!")
                end = True
        else: # not win
            status = raw_input("Would you like to continue? (Y/N) ")
            if status != "Y" or status != "y":
                print (Fore.BLUE + "Thank you for playing!")
                end = True

main()


'''
    try:
        usersize = int(raw_input("Please enter your level of difficulty (3 - 8): "))
    except ValueError:
        # a non-integer input
        print (Fore.RED + "Please input an integer from 3 - 8 only!")
        print "Reverting to default size 5", Fore.RESET
        usersize = 5
    if usersize < 3 or usersize > 8:
        print (Fore.RED + "Please input an integer from 3 - 8 only!")
        print "Reverting to default size 5", Fore.RESET
        usersize = 5

'''