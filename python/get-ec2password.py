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

""" 
#ec2 = session.connect_ec2() #access_key,secret_key
ec2 = session.resource('ec2', 'us-east-1')
i = ec2.connect_to_region()
passwd = base64.b64decode(i.get_password_data(instance_id))
if (passwd):
    with open (key_path,'r') as privkeyfile:
        priv = rsa.PrivateKey.load_pkcs1(privkeyfile.read())
    key = rsa.decrypt(passwd,priv)
else:
    key = 'Wait at least 4 minutes after creation before the admin password is available'
 
print(key)
"""

"""
ec2 = session.resource('ec2', 'us-east-1')
i = ec2.Instance('i-09cb4ca6676500e32')

enc_str = i.password_data()['']
with open('/Users/macadmin/pemkeys/ReleaseAutomation-Dev.pem') as fp:
  key = RSA.importKey(fp.read())

cipher = PKCS1_OAEP.new(key)
print(cipher.decrypt(enc_str))
"""

"""
# AWS S3
s3 = session.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
"""

###########################################################################################

"""
# AWS IAM
iam = session.client('iam')

# List users with the pagination interface
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)
"""
