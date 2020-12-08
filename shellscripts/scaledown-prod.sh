#!/bin/zsh

vared -p 'Input Service Name: ' -c srvName

kubectl get pods | grep $srvName | sed 's/-[0-9].*//' | while read LINE; do
#cat deploymentlist | while read LINE; do
    echo scaling down $LINE
    #kubectl scale deployments $LINE --replicas=0
done