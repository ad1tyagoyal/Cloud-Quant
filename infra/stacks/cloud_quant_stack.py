from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
)
from constructs import Construct

class CloudQuantStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None: # type: ignore
        super().__init__(scope, construct_id, **kwargs) # type: ignore
        
        self.raw_s3_bucket = s3.Bucket(
            self, "RawNifty50DataBucket",
            bucket_name="nifty-50-raw-data-bucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY
        )

