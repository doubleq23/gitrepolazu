import boto3,base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

###########################################################################################
#  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html  #
###########################################################################################

# Set AWS profile to be used
session = boto3.Session(profile_name='awsdevus')

###########################################################################################

instance_id = 'i-09cb4ca6676500e32'
key_path = '/Users/macadmin/pemkeys/ReleaseAutomation-Dev.pem'
region = 'us-east-1'

def decrypt(key_text, password_data):
    key = RSA.importKey(key_text)
    cipher = PKCS1_v1_5.new(key)
    return cipher.decrypt(base64.b64decode(password_data), None).decode('utf8')

with open(key_path, 'r') as key_file:
    key_text = key_file.read()

ec2_client = session.client('ec2', region)
response = ec2_client.get_password_data(InstanceId=instance_id)

print(decrypt(key_text, response['PasswordData']))

###########################################################################################