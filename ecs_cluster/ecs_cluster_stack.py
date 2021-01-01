from aws_cdk import core
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ecs_patterns as ecsPatterns


class EcsClusterStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.cluster = ecs.Cluster(self, "CdkCluster",
                                   cluster_name="cdk-ecs",
                                   vpc=vpc)
