import boto3

aws_profile = 'prodcloud'
aws_region = 'us-east-1'
instance_id = 'i-0a009476628fe543f'
ip_address = '10.15.59.170'

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
        print('Instance ID : ' + x['Instances'][0]['InstanceId'])
        print('Image ID    : ' + x['Instances'][0]['ImageId'])
        print('Key Name    : ' + x['Instances'][0]['KeyName'])
        print('IP Address  : ' + x['Instances'][0]['PrivateIpAddress'])
        print('Subnet ID   : ' + x['Instances'][0]['SubnetId'])

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
        print('Instance ID : ' + x['Instances'][0]['InstanceId'])
        print('Image ID    : ' + x['Instances'][0]['ImageId'])
        print('Key Name    : ' + x['Instances'][0]['KeyName'])
        print('IP Address  : ' + x['Instances'][0]['PrivateIpAddress'])
        print('Subnet ID   : ' + x['Instances'][0]['SubnetId'])


#getinstance(instance_id)
getinstance2(ip_address)