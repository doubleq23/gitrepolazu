import boto3

def getinstance(ipadd):
    aws_profile = 'prodcloud'
    aws_region = 'us-east-1'

    session = boto3.Session(profile_name=aws_profile)
    ec2_client = session.client('ec2', aws_region)

    #print('instance')

    describe = ec2_client.describe_instances(
        Filters=[
            {
                'Name':'instance-state-name',
                'Values':['running']
            },
            {
                'Name':'private-ip-address',
                'Values':[ipadd]
            }
        ]
    )

    for x in describe['Reservations']:
        #print(x['Instances'][0]['PrivateIpAddress'])
        instance_ID = x['Instances'][0]['InstanceId']

        tags = ec2_client.describe_tags(
            Filters=[
                {
                    'Name': 'resource-id',
                    'Values': [instance_ID]
                }
            ]
        )

        pkg_name = ''
        owner = ''
        #print(tags['Tags'][0])
        for y in tags['Tags']:
            if(y['Key']=="PackageName"):
                pkg_name = (y['Value']) # + ' ' + y['ResourceId'])
            if(y['Key']=="Owner"):
                owner = (y['Value']) # + ' ' + y['ResourceId'])
                
        print(instance_ID + ' | ipaddress : ' + ipadd + ' | owner : ' + owner + ' | package name : '+ pkg_name)
            

#############
#ip_address = ['10.15.3.110','172.17.3.233','172.17.3.254']
#ipa = ['10.15.5.54','10.15.57.225','172.17.3.233']

with open('ip3.txt') as my_file:
    ipa = my_file.readlines()

for ip_address in ipa:
    ipa_strip = ip_address.strip()
    print (ipa_strip)
    getinstance(ipa_strip)

#############

#getinstance(ip_address)
#privateIP = [Reservations][Instances][PrivateIpAddress]