import * as cdk from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as ecsPatterns from 'aws-cdk-lib/aws-ecs-patterns';
import * as logs from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';

export class AiPlatformStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, 'Vpc', {
      maxAzs: 2,
      natGateways: 1,
    });

    const cluster = new ecs.Cluster(this, 'Cluster', {
      vpc,
      containerInsights: true,
    });

    const service = new ecsPatterns.ApplicationLoadBalancedFargateService(this, 'Api', {
      cluster,
      cpu: 512,
      memoryLimitMiB: 1024,
      desiredCount: 2,
      publicLoadBalancer: true,
      taskImageOptions: {
        image: ecs.ContainerImage.fromRegistry('public.ecr.aws/docker/library/python:3.12-slim'),
        containerPort: 8000,
        logDriver: ecs.LogDrivers.awsLogs({
          streamPrefix: 'flowfusion-ai-api',
          logRetention: logs.RetentionDays.ONE_WEEK,
        }),
      },
    });

    service.targetGroup.configureHealthCheck({ path: '/health', healthyHttpCodes: '200' });

    const scaling = service.service.autoScaleTaskCount({ minCapacity: 2, maxCapacity: 10 });
    scaling.scaleOnCpuUtilization('CpuScaling', { targetUtilizationPercent: 60 });

    new cdk.CfnOutput(this, 'LoadBalancerDns', {
      value: service.loadBalancer.loadBalancerDnsName,
    });
  }
}
