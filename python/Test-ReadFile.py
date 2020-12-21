"""
f = open('ip.txt', 'r')
print(f.read())
f.close()
"""
#ip_address = ''

def readfromfile():
    f = open('ip.txt', 'r')
    ip_address = (f.readline()).replace("'", "")
    ip_add = ip_address.split(",")
    #print (ip_address)
    for ip in ip_add:
        print(ip)
    f.close()

"""
def readfromfile2():
    with open("ip.txt", "r") as f:
        ip_address = list(f)
        #print(ip_address)
        for ipadd in ip_address:
            print(ipadd + ' | ')

"""

readfromfile()
#print(ip_address)
#ip_address = "10.15.3.110,10.15.3.188,10.15.3.216"
#ip_address = '10.15.3.110', '10.15.3.188', '10.15.3.216'
#ipadd = ip_address.split(",")

#for ip in ip_address:
#    print(ip + ' | ')

#print('#############################')
#readfromfile2()

