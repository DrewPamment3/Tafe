#!/bin/python3.8
# version 1.5
# This program provides a rudimentary automation of IRTX
import IRTxModulesGit

print('Welcome to my IRTX tool')

def menu():
    choice = ''
    while choice != 0:
        print('What would you like to do?: ')
        choice = input('1 - Port Scan\n2 - Brute-force dvwa\n3 - Attempt brute-force\n\n0 - Exit tool\nchoice: ')
        if choice == '1':
            IRTxModulesGit.portscan()
        elif choice == '2':
            IRTxModulesGit.dvwa_brute()
        # elif choice == '3':
            IRTxModulesGit.unrealirc_backdoor()
        elif choice == '0':
            print('Goodbye...')
            input('Press <ENTER> to quit.')
            break
menu()
