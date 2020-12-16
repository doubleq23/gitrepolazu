import boto3
from modules import awsprofiles

awsprofiles.greeting("Lazu")

#aws_profile = awsprofiles.awsprofile("1")
#print(aws_profile)


# User Input
print("Select AWS profile to be used")
print("1. awsdevus")
print("2. awsqaus")
print("3. prodcloud")
profileselect = input ("Enter selection number: ")

aws_profile = awsprofiles.awsprofile(profileselect)
print("")
print("Using " + aws_profile + " profile")
