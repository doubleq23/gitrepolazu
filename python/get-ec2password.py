import boto3,base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

###########################################################################################
#  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html  #
###########################################################################################

########################################
#####    Variables & Parameters    #####
########################################
#instance_id = 'i-09cb4ca6676500e32'
region = 'us-east-1'
#priv_key_path = '/Users/macadmin/pemkeys/ReleaseAutomation-Dev.pem'

# Retrieve private key to be used
def keypath(i):
    switcher={
        'awsdevus':'/Users/macadmin/pemkeys/ReleaseAutomation-Dev.pem',
        'awsqaus':'/Users/macadmin/pemkeys/ReleaseAutomation-QA.pem',
        'prodcloud':'/Users/macadmin/pemkeys/ReleaseAutomation-ProdCloud-Key.pem'
    }
    return switcher.get(i,"Invalid private key")

# Retrieve AWS profile to be used
def awsprofile(i):
    switcher={
        '1':'awsdevus',
        '2':'awsqaus',
        '3':'prodcloud'
    }
    return switcher.get(i,"Invalid AWS Profile")

# Function to decrypt EC2 public key
def decrypt(key_text, password_data):
    key = RSA.importKey(key_text)
    cipher = PKCS1_v1_5.new(key)
    return cipher.decrypt(base64.b64decode(password_data), None).decode('utf8')

# User Input
print("Select AWS profile to be used")
print("1. awsdevus")
print("2. awsqaus")
print("3. prodcloud")
profileselect = input ("Enter selection number: ")
instance_id = input ("Enter Instance ID: ")

aws_profile = awsprofile(profileselect)
print("")
print("Using " + aws_profile + " profile")

key_path = keypath(aws_profile)
print("Decrypting password using " + key_path)
# Set AWS profile to be used

session = boto3.Session(profile_name=aws_profile)

# Read the provided private key
with open(key_path, 'r') as key_file:
    key_text = key_file.read()

# Connect to EC2 instance
ec2_client = session.client('ec2', region)
response = ec2_client.get_password_data(InstanceId=instance_id)

print(decrypt(key_text, response['PasswordData']))

###########################################################################################