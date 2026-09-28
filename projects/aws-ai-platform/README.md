# AWS AI Platform — TypeScript CDK

## Scenario
Provision repeatable infrastructure for a stateless AI API that needs multiple availability zones, load balancing, container orchestration, health checks, logs and horizontal scaling.

## Resources
- VPC across two AZs.
- ECS/Fargate cluster with Container Insights.
- Application Load Balancer.
- Two desired tasks with CPU autoscaling up to ten.
- CloudWatch log driver and health-check configuration.

## Validate without deploying
```bash
npm install
npm run build
npx cdk synth
```

`cdk synth` produces CloudFormation and is the primary traceable IaC artifact. Deployment requires an AWS account, bootstrapped CDK environment and a real application container image.

## Production hardening
Replace the demonstration image with ECR, add HTTPS/ACM, WAF, private application tasks where appropriate, VPC endpoints, Secrets Manager, task-role least privilege, KMS, alarms, budgets, image scanning and deployment strategies such as blue/green or canary.

This project demonstrates TypeScript programming plus AWS infrastructure-as-code rather than a console-built environment.