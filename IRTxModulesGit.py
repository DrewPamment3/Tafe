import nmap


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
        print(decision)
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
