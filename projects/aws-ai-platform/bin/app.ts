#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AiPlatformStack } from '../lib/ai-platform-stack';

const app = new cdk.App();
new AiPlatformStack(app, 'FlowFusionAiPlatform', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
