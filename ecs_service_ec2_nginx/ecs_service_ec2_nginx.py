from aws_cdk import core
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ecs_patterns as ecsPatterns
import aws_cdk.aws_applicationautoscaling as applicationautoscaling


class EcsServiceEc2Nginx(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, cluster, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        service = ecsPatterns.ApplicationLoadBalancedEc2Service(self, "nginx",
                                                                cluster=cluster,
                                                                memory_limit_mib=1024,
                                                                cpu=512,
                                                                task_image_options=ecsPatterns.ApplicationLoadBalancedTaskImageOptions(
                                                                    image=ecs.ContainerImage.from_registry(
                                                                        "nginx:stable"),
                                                                )
                                                                )

        target = service.service.auto_scale_task_count(min_capacity=1,
                                                       max_capacity=10)

        target.scale_on_request_count("ReqCountScalePolicy",
                                      requests_per_target=50,
                                      target_group=service.target_group)

        target.scale_on_schedule("TestSchedulePolicy",
                                 schedule=applicationautoscaling.Schedule.cron(hour="8", minute="0"),
                                 min_capacity=3
                                 )
