f = open('ip.txt', 'r')
print(f.read())
f.close()


def readfromfile():
    f = open('ip.txt', 'r')
    ip_address = [f.read()]
    print (ip_address)
    f.close()

def readfromfile2():
    with open("ip.txt", "r") as f:
        ip_address = list(f)
        #print(ip_address)
        for ipadd in ip_address:
            print(ipadd)