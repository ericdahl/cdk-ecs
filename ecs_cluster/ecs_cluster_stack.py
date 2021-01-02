from aws_cdk import core
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ec2 as ec2
import aws_cdk.core as cdk_core
import os


class EcsClusterStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, vpc, ec2_capacity=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.cluster = ecs.Cluster(self, "CdkCluster",
                                   cluster_name="cdk-ecs",
                                   vpc=vpc)

        if ec2_capacity:
            key_name = os.getenv("EC2_KEY_PAIR_NAME")
            asg = self.cluster.add_capacity("CdkClusterCapacity",
                                            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3_AMD,
                                                                              ec2.InstanceSize.SMALL),
                                            key_name=key_name,
                                            cooldown=cdk_core.Duration.seconds(30),
                                            min_capacity=1,
                                            max_capacity=5)

            # note: CDK doesn't support ECS capacity providers yet
            asg.scale_to_track_metric("CpuReservationScalingPolicy",
                                      metric=self.cluster.metric_cpu_reservation(),
                                      target_value=50)
            asg.scale_to_track_metric("MemoryReservationScalingPolicy",
                                      metric=self.cluster.metric_memory_reservation(),
                                      target_value=50)

            bastion = ec2.BastionHostLinux(self, "CdkBastion",
                                           vpc=vpc,
                                           subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC))
            bastion.allow_ssh_access_from(ec2.Peer.any_ipv4())
            bastion.instance.instance.key_name = key_name

            asg.connections.allow_from(bastion, ec2.Port.tcp(22))
