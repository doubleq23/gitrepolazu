import boto3
import time

# Set AWS profile to be used
session = boto3.Session(profile_name='awsdevus')

# Create cloudFront client
cf = session.client('cloudfront')

# Parameters
distribution_id = "EXXVMUQ03TUNJ"
distribution_path = "/*"

# Create cloudfront invalidation
invalidation = cf.create_invalidation(
    DistributionId=distribution_id,
    InvalidationBatch={
        'Paths': {
            'Quantity': 1,
            'Items': [distribution_path]
    },
        'CallerReference': str(time.time())
})

# Returns invalidation ID
print("Invalidation ID: " + invalidation['Invalidation']['Id'])


##################################################
"""
# Create S3 client
client = boto3.client('s3')

# Get distribution_id tag in S3 bucket
tags = client.get_bucket_tagging(Bucket=bucket_name)
for tag in tags["TagSet"]:
    if tag["Key"] == "distribution_id":
        distribution_id = tag["Value"]
        break
"""
##################################################