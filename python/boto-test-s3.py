import boto3

# Get AWS profile name
aws_profile = input ("Enter Aws profile: ")

# Set AWS profile to be used
session = boto3.Session(profile_name=aws_profile)

# AWS S3
s3 = session.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

######################################################