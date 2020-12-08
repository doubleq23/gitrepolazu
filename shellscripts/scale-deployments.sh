#!/bin/zsh

cat deploymentlist | while read LINE; do
    echo scaling down $LINE
    kubectl scale deployments $LINE --replicas=0
done