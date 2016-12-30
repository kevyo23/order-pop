#! /usr/bin/env python
# -*- coding: utf-8 -*-
# invent-a-story.py - exploring python dictionaries and collection module
# Kevin Yu on 30/12/2016

import collections

# syntax to display a dictionary
def display_dictionary(dictionary, title, is_formatted):
    sorted_dict = sort_inventory(dictionary)
    if is_formatted: formatted_display(sorted_dict, title)
    else: standard_display(sorted_dict, title)
    print('\n')

# from: display_dictionary -> without allignment
def standard_display(dictionary, title):
    print(title)
    item_total = 0
    for k, v in dictionary.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

# from: display_dictionary -> with allignment
def formatted_display(dictionary, title):
    item_total = 0
    L = 24
    R = 6
    # dynamic adjustment according to user item input
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
    
# add or take an item in an existing inventory
# item_data is a list of ['@command', 'item name', number of items]
def edit_item(inventory, item_data, is_add):
    item_value = inventory.setdefault(item_data[1], 0)
    if int(item_data[2]) > 1000000:
        print('Number entered exceeds limit')
    elif len(item_data[1]) > 72:
        print('Item name cannnot be longer than 72 characters')
    else:
        if is_add:
            if item_value == 0:
                print(item_data[1] + ' has been added')
            item_value += int(item_data[2])
        else:
            if item_value == 0:
                print('Can\'t take from an item not in the inventory!')
                return inventory
            item_value -= int(item_data[2])
        inventory[item_data[1]] = item_value
        if item_value <= 0:
            print(item_data[1] + ' has been removed')
            del inventory[item_data[1]]
    return inventory

# rearrange dictionary in reverse sorted order (greatest item value first)
def sort_inventory(inventory):
    return collections.OrderedDict(sorted(inventory.items(), key = lambda t: t[1], reverse=True))

# retrieve user data
def collect(contents):
    action_string = '@add @take @clear'
    print('Enter \'@add, item, number\' to add \'number\' of \'item\' into the inventory')
    print('Enter \'@take, item, number\' to take \'number\' of \'item\' from the inventory')
    print('Enter \'@clear\' as an item to clear entire inventory')

    while True:
        new = raw_input().split(', ')
        # handle all invalid cases
        if new[0] == '@clear':
            contents = {}
            break
        elif len(new) != 3:
            print('Unless using \'@clear\', three values must be entered')
        elif new[0] not in action_string:
            print('Invalid command entered')
        elif not new[2].isdigit():
            print('Number must contain digits only')
        else:
            # alter inventory
            new[1] = new[1].title()
            if new[0] == '@add':
                contents = edit_item(contents, new, True) 
            elif new[0] == '@take':
                contents = edit_item(contents, new, False)
            break
    return contents

# main function
def main():
    no_string = 'No no N n'
    print('Invent-a-story. Carve your own story! Enter items you would like to add to your inventory!')
    if raw_input('Would you like to load a premade inventory? ') in no_string:
        contents = {}
    else:
        print('Here\'s a start:')
        contents = {'Torch': 1, 'Water': 6, 'Dollar Bill': 42, 'Laptop': 1, 'Food': 12}
        contents = sort_inventory(contents)
    display_dictionary(contents, 'My inventory', True)
    while True:
        contents = collect(contents)
        display_dictionary(contents, 'My inventory', True)
        if raw_input('Continue? (Yes/No) ') in no_string:
            break
main()
