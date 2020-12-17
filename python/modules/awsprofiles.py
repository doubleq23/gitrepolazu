# Retrieve AWS profile to be used
def awsprofile(i):
    switcher={
        '1':'awsdevus',
        '2':'awsqaus',
        '3':'prodcloud'
    }
    return switcher.get(i,"Invalid AWS Profile")

#print(awsprofile("1"))

####   Example   ####
def greeting(name):
    print("Hello, " + name)