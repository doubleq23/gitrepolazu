# Retrieve private key to be used
def keypath(i):
    switcher={
        'awsdevus':'/Users/macadmin/pemkeys/ReleaseAutomation-Dev.pem',
        'awsqaus':'/Users/macadmin/pemkeys/ReleaseAutomation-QA.pem',
        'prodcloud':'/Users/macadmin/pemkeys/ReleaseAutomation-ProdCloud-Key.pem'
    }
    return switcher.get(i,"Invalid private key")

#print(keypath('awsdevus'))