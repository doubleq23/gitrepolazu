import boto3,base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

###########################################################################################
#  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html  #
###########################################################################################

################################################
#####    Variables & Parameters            #####
################################################

#instance_id = 'i-09cb4ca6676500e32'
aws_region = 'us-east-1'
#priv_key_path = '/Users/macadmin/pemkeys/ReleaseAutomation-Dev.pem'


#####################################################
#####  Retrieve private key to be used          #####
#####################################################

def keypath(i):
    switcher={
        'awsdevus':'/Users/macadmin/pemkeys/ReleaseAutomation-Dev.pem',
        'awsqaus':'/Users/macadmin/pemkeys/ReleaseAutomation-QA.pem',
        'prodcloud':'/Users/macadmin/pemkeys/ReleaseAutomation-ProdCloud-Key.pem'
    }
    return switcher.get(i,"Invalid private key")


#####################################################
#####  Retrieve AWS profile to be used          #####
#####################################################

def awsprofile(i):
    switcher={
        '1':'awsdevus',
        '2':'awsqaus',
        '3':'prodcloud'
    }
    return switcher.get(i,"Invalid AWS Profile")


#####################################################
#####  Function to decrypt EC2 public key       #####
#####################################################

def decrypt(key_text, password_data):
    key = RSA.importKey(key_text)
    cipher = PKCS1_v1_5.new(key)
    return cipher.decrypt(base64.b64decode(password_data), None).decode('utf8')


#####################################################
#####  Get instance details                     #####
#####################################################

def getinstance(user_input):
    session = boto3.Session(profile_name=aws_profile)
    ec2_client = session.client('ec2', aws_region)

    if (user_input.startswith('i-')):
        describe = ec2_client.describe_instances(
            Filters=[
                {
                    'Name':'instance-state-name',
                    'Values':['running']
                },
                {
                    'Name':'instance-id',
                    'Values':[user_input]
                }
            ]
        )
    else:
        describe = ec2_client.describe_instances(
            Filters=[
                {
                    'Name':'instance-state-name',
                    'Values':['running']
                },
                {
                    'Name':'private-ip-address',
                    'Values':[user_input]
                }
            ]
        )

    for x in describe['Reservations']:
        AWSInstanceID = x['Instances'][0]['InstanceId']
        AWSIPaddress = x['Instances'][0]['PrivateIpAddress']
        AWSImageID = x['Instances'][0]['ImageId']
        AWSKeyName = x['Instances'][0]['KeyName']
        AWSSubnetID = x['Instances'][0]['SubnetId']
    
    return AWSInstanceID,AWSIPaddress,AWSImageID,AWSKeyName,AWSSubnetID


#######################################################
#####  User Input Selection                       #####
#######################################################

print("Select AWS profile to be used")
print("1. awsdevus")
print("2. awsqaus")
print("3. prodcloud")
profileselect = input ("Enter AWS profile selection number : ")
user_input = input ("Enter Instance ID or IP address    : ")


#####  Getting selection  #####
aws_profile = awsprofile(profileselect)
key_path = keypath(aws_profile)

#####  Getting instance details  #####
InstanceDetails = getinstance(user_input)
    
#####  Set AWS profile to be used and connect to EC2 instance  #####
session = boto3.Session(profile_name=aws_profile)
ec2_client = session.client('ec2', aws_region)
response = ec2_client.get_password_data(InstanceId=InstanceDetails[0])

#####  Read the provided private key  #####
with open(key_path, 'r') as key_file:
    key_text = key_file.read()

#####  Decrypt password data  #####
pwd_data = decrypt(key_text, response['PasswordData'])


#######################################################
#####  Output                                     #####
#######################################################

print("")
print("AWS profile : " + aws_profile)
#print("AWS keypath : " + key_path)
print("Instance ID : " + InstanceDetails[0])
print("IP Address  : " + InstanceDetails[1])
print("Credential  : " + pwd_data)
print("")
print("")


###########################################################################################