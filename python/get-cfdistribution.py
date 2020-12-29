import boto3

###########################################################################################
#  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html  #
###########################################################################################

# Set AWS profile to be used
session = boto3.Session(profile_name='awsdevus')

###########################################################################################

# Create CloudFront client
cf = session.client('cloudfront')

# List distributions
print("\nCloudFront Distributions:\n")
distributions=cf.list_distributions()
if distributions['DistributionList']['Quantity'] > 0:
  #if distributions['DistributionList']['Items']['Enabled'] = True
  for distribution in distributions['DistributionList']['Items']:
    print("Domain: " + distribution['DomainName'])
    print("Distribution Id: " + distribution['Id'])
    print("Comment: " + distribution['Comment'])
    #print("Origin Domain Name: " + distribution['Origins']['Items']['DomainName'])        <-------  This is currently NOT WORKING
    """print("Certificate Source: " + distribution['ViewerCertificate']['CertificateSource'])
    if (distribution['ViewerCertificate']['CertificateSource'] == "acm"):
      print("Certificate: " + distribution['ViewerCertificate']['Certificate'])"""
    print("")
else:
  print("Error - No CloudFront Distributions Detected.") 