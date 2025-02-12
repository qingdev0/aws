import pytest
from aws_lambda_powertools.utilities.typing import LambdaContext

@pytest.fixture
def lambda_context():
    class MockLambdaContext(LambdaContext):
        function_name: str = "test-function"
        function_version: str = "$LATEST"
        invoked_function_arn: str = "arn:aws:lambda:us-east-1:123456789012:function:test-function"
        memory_limit_in_mb: int = 128
        aws_request_id: str = "test-request-id"
        log_group_name: str = "/aws/lambda/test-function"
        log_stream_name: str = "2024/03/01/[$LATEST]123456789012"

    return MockLambdaContext() 