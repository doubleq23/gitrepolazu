import boto3

# Set AWS profile to be used
session = boto3.Session(profile_name='awsdevus')

# AWS S3
s3 = session.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

######################################################