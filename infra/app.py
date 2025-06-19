#!/usr/bin/env python3
import aws_cdk as cdk

from infra.stacks.cloud_quant_stack import CloudQuantStack


app = cdk.App()
CloudQuantStack(app, "CloudQuantStack")

app.synth()
