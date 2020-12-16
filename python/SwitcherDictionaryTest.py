
def keypath(i):
    switcher={
        1:'/Users/macadmin/pemkeys/ReleaseAutomation-Dev.pem',
        2:'/Users/macadmin/pemkeys/ReleaseAutomation-QA.pem',
        3:'/Users/macadmin/pemkeys/ReleaseAutomation-ProdCloud-Key.pem'
    }
    return switcher.get(i,"Invalid private key")

#print(keypath('prod'))

# User Input
print("Select AWS profile to be used")
print("1. awsdevus")
print("2. awsqaus")
print("3. prodcloud")
aws_profile = input ("Enter selection number: ")
#print(aws_profile)
#print(type(aws_profile))
def awsprofile(i):
    switcher={
        '1':'awsdevus',
        '2':'awsqaus',
        '3':'prodcloud'
    }
    return switcher.get(i,"Invalid AWS Profile")

print(awsprofile(aws_profile))

def week(i):
    switcher={
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }
    return switcher.get(i,"Invalid day of week")

#w = week(2)
#print('Today is ' + week(2))