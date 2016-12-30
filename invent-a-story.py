#! /usr/bin/env python
# -*- coding: utf-8 -*-
# invent-a-story.py - exploring python dictionaries and collection module
# Kevin Yu on 30/12/2016

#TODO

# remove items
# clear dictionary
# not using lists

import collections

# syntax to display a dictionary
def display_dictionary(dictionary, title, is_formatted):
    if is_formatted: formatted_display(dictionary, title)
    else: standard_display(dictionary, title)
    print('\n')

# without allignment
def standard_display(dictionary, title):
    print(title)
    item_total = 0
    for k, v in dictionary.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

# with allignment
def formatted_display(dictionary, title):
    item_total = 0
    L = 24
    R = 6
    for k, v in dictionary.items():
        if len(k) > L:
            L = len(k)
        item_total += v
    if len(str(item_total)) > R:
        R = len(str(item_total))
    print(title.center(L + R, '-'))
    for k, v in dictionary.items():
        print(k.ljust(L, '.') + (str(v).rjust(R)))
    print('Total number of items: '.ljust(L, ' ') + str(item_total).rjust(R))
    

# add a list of items into an existing inventory
def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        inventory.setdefault(added_items[i], 0)
        inventory[added_items[i]] += 1
    return sort_inventory(inventory)

# transform an unordered list of items to a new inventory
def normalise_list(added_items):
    new_inventory = {}
    for i in range(len(added_items)):
        new_inventory.setdefault(added_items[i], 0)
        new_inventory[added_items[i]] += 1
    return sort_inventory(new_inventory)

# combine secondary inventory into the primary
def combine_inventory(primary_inv, secondary_inv):
    for k, v in secondary_inv.items():
        primary_inv.setdefault(k, 0)
        primary_inv[k] += v
    return sort_inventory(primary_inv)

# rearrange dictionary in reverse sorted order (greatest item value first)
def sort_inventory(inventory):
    return collections.OrderedDict(sorted(inventory.items(), key = lambda t: t[1], reverse=True))

def collect():
    user_list = []
    print('Please type your list of items, separated by an enter:')
    print('To duplicate an item, enter \'@dup\' as a following entry after you have entered the item')
    print('To add a template list, enter \'@example\' as an item')
    print('When done, enter \'@done\' as an item')

    while True:
        new = raw_input()
        if new == '@done':
            break
        if new == '@example':
            user_list = ['dollar bill', 'food', 'dollar bill', 'dollar bill', 'ruby']
            break
        if new == '':
            print('You can\'t add an empty item value!')
            continue
        if len(new) > 72:
            print('Character count too long.. Please enter a shorter item')
            continue
        if new == '@dup':
            if len(user_list) == 0:
                print('Only enter @dup after you have declared the item you want to duplicate')
            else:
                print('How many times would you like to duplicate?')
                while True:
                    print('Enter a multiplier:')
                    mult = raw_input()
                    if not mult.isdigit() or int(mult) < 1 or int(mult) > 100:
                        print('Please only enter a positive integer from 1-100')
                        continue
                    break
                for i in range(int(mult)):
                    user_list.append(old)
        else:
          user_list.append(new)
          old = new
    return user_list
    
def main():
    print('Invent-a-story. Carve your own story! Enter items you would like to add to your inventory!')
    print('Here\'s a start:')
    contents = {'torch': 1, 'water': 6, 'dollar bill': 42, 'laptop': 1, 'food': 12}
    contents = sort_inventory(contents)
    display_dictionary(contents, 'My inventory', True)
    while True:
        add_list = collect()
        new_items = normalise_list(add_list)
        display_dictionary(new_items, 'Items collected', False)
        contents = combine_inventory(contents, new_items )
        display_dictionary(contents, 'My inventory', True)
        response_string = 'No no N n Exit exit Quit quit'
        if raw_input('Add more? (Yes/No) ') in response_string:
            break
main()
