# This program provides a rudimentary way to scan targets and manipulate output
import IRTxModulesGit


def menu():
    choice = ''
    while choice != 0:
        print('Welcome to my IRTX tool\n What would you like to do?: ')
        choice = input('1 - Port Scan\n2 - Attempt exploit\n3 - Attempt brute-force\n\n0 - Exit tool\nchoice: ')
        if choice == '1':
            IRTxModulesGit.portscan()
        elif choice == '2':
            Exploit()
        elif choice == '3':
            Brute-force()
        elif choice == '0':
            print('Goodbye...')
            input('Press <ENTER> to quit.')
            break
menu()