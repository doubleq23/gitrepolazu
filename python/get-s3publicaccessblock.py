import boto3

# Variables & Parameters
#awsprofile='awsdevus'
s3bucketname = 'ghimtest'
awsprofile = input ("Enter Aws profile: ")


# Set AWS profile & Connect to AWS S3 session
session = boto3.Session(profile_name=awsprofile)
s3 = session.resource('s3')
s3bucket = session.client('s3')

# Print out bucket names
def listbucketname():
    for bucket in s3.buckets.all():
        print(bucket.name)

# Set the public access block
def settingpublicaccessblock():
    setpublicaccessblock = s3bucket.put_public_access_block(
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        },
        Bucket=s3bucketname
    )

# Retrieve a bucket's public access setting

def getbucketacl():
    aclresult = s3bucket.get_bucket_acl(Bucket=s3bucketname)
    print(aclresult)

def getpolicyresult():
    policyresult = s3bucket.get_bucket_policy(Bucket=s3bucketname)
    print(policyresult['Policy'])

def getpublicaccessblock():
    publicaccessblock = s3bucket.get_public_access_block(Bucket=s3bucketname)
    print(publicaccessblock['PublicAccessBlockConfiguration'])

####################
###     Main     ###
####################

getpublicaccessblock()
#settingpublicaccessblock()
#listbucketname()