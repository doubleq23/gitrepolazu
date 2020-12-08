#!/bin/bash
# Read CF Distribution ID string with spaces using for loop
declare -a CF_Distribution_ID=("EAA7Z475MDVLK" "E2DSN03KAVPF1Z" "E1AMA6NTSCNRHI" "ED8FCGKPTUG0L" "EBGCLMPKX7U0P" "EZ43BHWCLU6F0" "E1GZ4T3L6SO709" "E2PGDGT6I4L9BC" "E1N7T4PNPQKNG" "EKHBO96PD27QB" "E1TNRC8YPBG86H" "E1FDLF80S1751G" "E2H0DD39CFM4ME" "E37WMLFVXFVRJI" "E3IRYBIWB9MV8N" "E1U50HHAJB0BBL" "E1TMQGQV1JM2VK")
#declare -a CF_Distribution_ID=("EXXVMUQ03TUNJ")
awsprofile="prodcloud"

# Iterate the string array using for loop
for cfid in "${CF_Distribution_ID[@]}"
do
    #echo Invalidating $cfid
    #aws cloudfront list-distributions --query "DistributionList.Items[*].{id:Id,comment:Comment}[?id=='$cfid'].comment" --output text --profile=prodcloud
    comment=$(aws cloudfront get-distribution --id $cfid --profile=$awsprofile --query Distribution.DistributionConfig.Comment --output text)
    echo Invalidating $cfid $comment
    invalidate=$(aws cloudfront create-invalidation --profile=$awsprofile --distribution-id $cfid --paths "/*" --query Invalidation.Id --output text)
    echo Invalidation created. ID is $invalidate
done

#read -s -d ' '

#aws cloudfront list-distributions --query "DistributionList.Items[*].{id:Id,origin:Origins.Items[0].Id}[?origin=='S3-BUCKET_NAME'].id" --output text

#for id in $(aws cloudfront list-distributions --query "DistributionList.Items[*].{id:Id,origin:Comment}[?comment=='coda'].id" --output text);do aws cloudfront create-invalidation --distribution-id $id --paths "/*";done;

#aws cloudfront list-distributions --query "DistributionList.Items[*].{id:Id,origin:Comment}[?comment=='coda'].id" --output text --profile=prodcloud
#aws cloudfront list-distributions --query "DistributionList.Items[*].{id:Id,origin:Origins.Items[0].DomainName}[?origin=='www.gslb.monster.com'].id" --output text --profile=prodcloud