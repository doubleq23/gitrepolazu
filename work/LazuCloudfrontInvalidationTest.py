"""
Cloudfront Invalidation
"""

from __future__ import print_function
import boto3
import time

def selectcloudfront(selection,selectionparam,cfpath):
    client = boto3.client('cloudfront')
    list = client.list_distributions()
    #print('client select cloudfront')

    for distribution in list['DistributionList']['Items']:
        if selection == '1' or selection == '2':
            if distribution['Comment'].startswith(selectionparam):
                print(distribution['Comment'])
                invalidate(client,distribution['Id'],cfpath)
        elif selection == '3':
            if distribution['Id'] == selectionparam:
                print(distribution['Comment'])
                invalidate(client,distribution['Id'],cfpath)

def invalidate (client,distID,cfpath):
    #print ('client invalidate')
    #print(distID)
    
    invalidation = client.create_invalidation (
        DistributionId=distID,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [cfpath]
            },
            'CallerReference': str(time.time())
        }
    )
    
    #print(invalidation)
    print('Invalidate success')

def lambda_handler(event, context):
    print('start')
    path = event["path"]
    selection = event['selection']
    
    if selection == '1':
        selectionparam = 'www.monster'
        selectcloudfront(selection,selectionparam,path)
        #print(selection)
        
    elif selection == '2':
        selectionparam = 'manage.monster'
        selectcloudfront(selection,selectionparam,path)
        #print(selection)
        
    elif selection == '3':
        selectionparam = event['distID']
        selectcloudfront(selection,selectionparam,path)
        #print(selection)