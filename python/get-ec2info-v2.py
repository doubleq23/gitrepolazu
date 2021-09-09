import boto3

aws_profile = 'awsdevus'
aws_region = 'us-east-1'
instance_id = 'i-075b48ad6683b47b2'
ip_address = '10.167.25.114'

def getinstance(instanceid):
    session = boto3.Session(profile_name=aws_profile)
    ec2_client = session.client('ec2', aws_region)

    describe = ec2_client.describe_instances(
        Filters=[
            {
                'Name':'instance-state-name',
                'Values':['running']
            },
            {
                'Name':'instance-id',
                'Values':[instanceid]
            }
        ]
    )
    #print(describe)

    for x in describe['Reservations']:
        print('get instance from instance ID')
        print('Instance ID : ' + x['Instances'][0]['InstanceId'])
        print('Image ID    : ' + x['Instances'][0]['ImageId'])
        print('Key Name    : ' + x['Instances'][0]['KeyName'])
        print('IP Address  : ' + x['Instances'][0]['PrivateIpAddress'])
        print('Subnet ID   : ' + x['Instances'][0]['SubnetId'])
        print(' ')

def getinstance2(ipadd):
    session = boto3.Session(profile_name=aws_profile)
    ec2_client = session.client('ec2', aws_region)

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
    #print(describe)
    #print(['Reservations']['Instances'][0]['InstanceId'])

    for x in describe['Reservations']:
        print('get instance from IP address')
        print('Instance ID : ' + x['Instances'][0]['InstanceId'])
        print('Image ID    : ' + x['Instances'][0]['ImageId'])
        print('Key Name    : ' + x['Instances'][0]['KeyName'])
        print('IP Address  : ' + x['Instances'][0]['PrivateIpAddress'])
        print('Subnet ID   : ' + x['Instances'][0]['SubnetId'])
        print(' ')


getinstance(instance_id)
getinstance2(ip_address)