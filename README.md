# cdk-ecs

Demo app illustrating use of CloudFormation Development Kit (CDK) to create Elastic Container Service (ECS) resources.

This app creates:

- VPC Stack
- ECS Cluster Stack
- multiple ECS Service Stacks

## Quick start

```
# Setup environment

$ git clone ...
$ cd cdk-ecs
$ python3.7 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt

# Deploy Stacks

$ cdk deploy --all
...

Outputs:
cdk-ecs-fargate-nginx.nginxLoadBalancerDNS19CE8D72 = cdk-e-nginx-1W4VIZUD1XMEM-1557887656.us-east-1.elb.amazonaws.com
cdk-ecs-fargate-nginx.nginxServiceURL39DAA5BC = http://cdk-e-nginx-1W4VIZUD1XMEM-1557887656.us-east-1.elb.amazonaws.com

```

## Other commands

```
# show changes to be made
$ cdk diff --all

# show CloudFormation scripts that are used
$ cdk synth

```

## Clean up

```
$ cdk destroy --all
```