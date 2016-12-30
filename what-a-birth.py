#! /usr/bin/env python
# -*- coding: utf-8 -*-
# what-a-birth.py - simple birthday monitor, check and add birthdays
# Kevin Yu on 28/12/2016

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
all_months = 'January February March April May June July August September October November December'

while True:
    print('Enter a name: (blank to quit)')
    name = raw_input()
    if name == '':
        break
    if not name.isalpha():
        print ('Invalid name entered - must contain letters only, eg Daniel')
        continue
    name = name.title()

    if name in birthdays:
        print(name + ' has a birthday on ' + birthdays[name])
    else:
        print('No birthday record found for ' + name)
        print('What month is ' + name + '\'s birthday?')
        while True:
            print('Enter a month:')
            month = raw_input()
            if not name.isalpha() or month.title() not in all_months:
                print('Invalid month entered - must contain letters only, eg January')
                continue
            break
        month = month.title()
        month = month[:3]
        while True:
            print('Enter a date:')
            date = raw_input()
            if not date.isdigit() or int(date) < 1 or int(date) > 31:
                print('Invalid date entered - must contain numbers only, eg 21')
                continue
            break
        birthdays[name] = month + ' ' + date
        print ('Birthday database updated.')
