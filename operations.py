#!/usr/bin/env python

import os
import random
import numpy
import operator

def create_list():
    list = []
    for i in range(4):
        list.append(random.randint(1,10))
    return list

def create_value(shuff, ops):
    return eval(str(shuff[0]) + ops[0] + str(shuff[1]) + ops[1] + str(shuff[2]) + ops[2] + str(shuff[3]))
    '''
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '/':operator.truediv}
    '''

def main():

    win = False
    attempts = 0
    nums = create_list()
    shuff = list(nums)
    random.shuffle(shuff)
    ops = list('+-*')
    random.shuffle(ops)
    value = create_value(shuff, ops)
    print "Welcome to guess the order\n==========================="
    #print "\nI'm thinking of a number, you have to guess what it is.\n"
    print "Here are a list of random numbers"
    print ' '.join(map(str, nums))
    print "Here are a list of operations, in order"
    print ' '.join(ops)
    print "Please enter the numbers in correct order to give ", value
    print "Note operation priority i.e. * before + or -"

    while win != True:
        if attempts > 10:
            print "Game over, correct order is ", ' '.join(map(str, shuff))
            return
        user = map(int, raw_input().split())
        attempts = attempts + 1
        if user.__len__() == shuff.__len__():
            uservalue = create_value(user,ops)
        else:
            print user.__len__(), "input values detected. Trying to be smart, are we?"
            continue
        shuff.sort()
        user.sort()
        if shuff == user:
            if uservalue == value:
                print "===========================\nWell done, that is correct!"
                win = True;
            else:
                print "Incorrect, your order gives ",uservalue
        else:
            print "Incorrect input detected. Please use values provided"
main()
