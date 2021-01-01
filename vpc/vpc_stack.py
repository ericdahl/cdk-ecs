from aws_cdk import core
import aws_cdk.aws_ec2 as ec2


class VpcStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(self, "VPC",
                           nat_gateways=1,
                           subnet_configuration=[
                               ec2.SubnetConfiguration(name="public", subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24),
                               ec2.SubnetConfiguration(name="private", subnet_type=ec2.SubnetType.PRIVATE,
                                                       cidr_mask=24),
                               ec2.SubnetConfiguration(name="isolated", subnet_type=ec2.SubnetType.ISOLATED,
                                                       cidr_mask=24)
                           ],
                           gateway_endpoints={
                               "S3": ec2.GatewayVpcEndpointOptions(
                                   service=ec2.GatewayVpcEndpointAwsService.S3
                               )
                           },
                           flow_logs={"FlowLogs": ec2.FlowLogOptions()})
