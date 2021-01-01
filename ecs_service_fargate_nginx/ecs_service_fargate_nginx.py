from aws_cdk import core
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ecs_patterns as ecsPatterns


class EcsServiceFargateNginx(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, cluster, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ecsPatterns.ApplicationLoadBalancedFargateService(self, "nginx",
                                                          cluster=cluster,
                                                          memory_limit_mib=1024,
                                                          cpu=512,
                                                          task_image_options=ecsPatterns.ApplicationLoadBalancedTaskImageOptions(
                                                              image=ecs.ContainerImage.from_registry("nginx:stable"),
                                                          )
                                                          )
