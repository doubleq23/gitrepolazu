import requests,shutil

###  Global Parameter  ###

hoststempfolder = '/Users/macadmin/Documents/hostsfiles/'
hostsdest = '/etc/hosts'
hostsoriginal = '/etc/hosts_original'

###  User Input  ###
print("Select hosts file to be used")
print("1. DEVE hosts")
print("2. QA10 hosts")
print("3. QA12 hosts")
print("4. QAX1 hosts")
print("5. QAX2 hosts")
print("6. QAX5 hosts")
print("7. QAX6 hosts")
print("8. Refresh Prod")
selecthosts = input ("Enter selection number: ")


###  Selector  ###
def hostsselected(i):
    switcher={
        '1':'DEVE',
        '2':'QA10',
        '3':'QA12',
        '4':'QAX1',
        '5':'QAX2',
        '6':'QAX5',
        '7':'QAX6',
        '8':'PROD'
    }
    return switcher.get(i,"Invalid input") #print(hostsselected(selecthosts))
hosts_selected = hostsselected(selecthosts)

def hostsurl(i):
    switcher={
        'DEVE' : 'http://env.monster.com/Documents/Releases/Site.2021/DevE-hosts.txt',
        'QA10' : 'http://qa.monster.com/hosts/QA10-hosts.txt',
        'QA12' : 'http://qa.monster.com/hosts/QA12-hosts.txt',
        'QAX1' : 'http://qa.monster.com/hosts/QAX1-hosts.txt',
        'QAX2' : 'http://qa.monster.com/hosts/QAX2-hosts.txt',
        'QAX5' : 'http://qa.monster.com/hosts/QAX5-hosts.txt',
        'QAX6' : 'http://qa.monster.com/hosts/QAX6-hosts.txt',
        'PROD' : ''
    }
    return switcher.get(i,"Invalid input") #print(hostsurl(hosts_selected))
hosts_url = hostsurl(hosts_selected)

###  Download hostsfile from the given URL  ###
def download_hosts():
    if (hosts_selected == 'PROD'):
        copy_hosts()
    else:
        print("Downloading " + hosts_selected + " hostsfile")
        r = requests.get(hosts_url, allow_redirects=True)
        open(hoststempfolder + hosts_selected, 'wb').write(r.content)
        print("Download completed")
        copy_hosts()

###  Replace current hosts file with the downloaded hostsfile  ###
def copy_hosts():
    if (hosts_selected == 'PROD'):
        print("Refresh PROD")
        shutil.copyfile (hostsoriginal, hostsdest)
        print("Refresh PROD completed")
    else:
        print("Copying hostsfile")
        shutil.copyfile (hoststempfolder + hosts_selected, hostsdest)
        print("Copy completed")

###  Main Function  ###
download_hosts()