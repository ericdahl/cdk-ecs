from aws_cdk import core
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ec2 as ec2


class EcsClusterStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, vpc, ec2_capacity=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.cluster = ecs.Cluster(self, "CdkCluster",
                                   cluster_name="cdk-ecs",
                                   vpc=vpc)

        if ec2_capacity:
            asg = self.cluster.add_capacity("CdkClusterCapacity",
                                            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3_AMD,
                                                                              ec2.InstanceSize.SMALL))
