import boto3
from modules import awsprofiles, awskeypairs

#awsprofiles.greeting("Lazu")
#aws_profile = awsprofiles.awsprofile("1")
#print(aws_profile)


# User Input
print("Select AWS profile to be used")
print("1. awsdevus")
print("2. awsqaus")
print("3. prodcloud")
profileselect = input ("Enter selection number: ")

aws_profile = awsprofiles.awsprofile(profileselect)
key_path = awskeypairs.keypath(aws_profile)
print("")
print("Using profile : " + aws_profile)
print("Using keypath : " + key_path)