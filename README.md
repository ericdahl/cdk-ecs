# cdk-ecs

Demo app illustrating use of CloudFormation Development Kit (CDK) to create Elastic Container Service (ECS) resources.

This app creates:

- VPC Stack
- ECS Cluster Stack
- multiple ECS Service Stacks

## Quick start

```
# create a venv using requirements.txt and source it

$ cdk deploy --all

...

Outputs:
cdk-ecs-fargate-nginx.nginxLoadBalancerDNS19CE8D72 = cdk-e-nginx-1W4VIZUD1XMEM-1557887656.us-east-1.elb.amazonaws.com
cdk-ecs-fargate-nginx.nginxServiceURL39DAA5BC = http://cdk-e-nginx-1W4VIZUD1XMEM-1557887656.us-east-1.elb.amazonaws.com

```

## Clean up

```
$ cdk destroy --all
```