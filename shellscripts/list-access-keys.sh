#!/bin/sh
for i in $(cat PRODENG-2753-users)
do
  echo "Checking user $i"
  aws iam list-access-keys --user-name $i --profile=awsdevus
done
