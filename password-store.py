#! /usr/bin/env python
# -*- coding: utf-8 -*-
# password-store.py - exploring file read/writing and shelve module
# Kevin Yu on 11/01/2017

import shelve

def main():
    print('WARNING: This is an insecure password manager. Use at own discretion.')
    passwordShelf = shelve.open('configData')
    while True:
        if len(passwordShelf.keys()) == 0:
            print('No passwords currently in system.')
        else:
            print('Displaying current accounts with passwords stored:')
            print ', '.join(passwordShelf.keys())
        print('Enter an existing account to retrieve password, or type a new account to add.')
        account = raw_input()
        if account == '':
            passwordShelf.close()
            break
        if account not in passwordShelf:
            print('Enter the password for this account.')
            password = raw_input()
            passwordShelf[account] = password
        print('Username: ' + account + ', Password: ' + passwordShelf[account])

main()
