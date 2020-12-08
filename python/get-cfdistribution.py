import boto3

# Set AWS profile to be used
session = boto3.Session(profile_name='awsdevus')

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
    print("Certificate Source: " + distribution['ViewerCertificate']['CertificateSource'])
    if (distribution['ViewerCertificate']['CertificateSource'] == "acm"):
      print("Certificate: " + distribution['ViewerCertificate']['Certificate'])
    print("")
else:
  print("Error - No CloudFront Distributions Detected.") 