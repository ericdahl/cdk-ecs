#!/usr/bin/env python3

from aws_cdk import core

from vpc.vpc_stack import VpcStack
from ecs_cluster.ecs_cluster_stack import EcsClusterStack
from ecs_service_fargate_nginx.ecs_service_fargate_nginx import EcsServiceFargateNginx
from ecs_service_ec2_nginx.ecs_service_ec2_nginx import EcsServiceEc2Nginx

app = core.App()

vpc_stack = VpcStack(app, "cdk-vpc")
ecs_cluster_stack = EcsClusterStack(app,
                                    "cdk-ecs",
                                    vpc=vpc_stack.vpc,
                                    ec2_capacity=True)

ecs_service_fargate_nginx_stack = EcsServiceFargateNginx(app,
                                                         "cdk-ecs-fargate-nginx",
                                                         cluster=ecs_cluster_stack.cluster)

ecs_service_ec2_nginx_stack = EcsServiceEc2Nginx(app,
                                                 "cdk-ecs-ec2-nginx",
                                                 cluster=ecs_cluster_stack.cluster)

app.synth()
