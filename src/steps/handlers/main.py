"""
AWS Lambda handler for processing API Gateway requests and SNS messages.
Includes functionality to trigger GitHub Actions workflows based on SNS messages.
"""

import requests
from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

from steps.services.sns import process_message

logger = Logger()
tracer = Tracer()
metrics = Metrics()
app = APIGatewayRestResolver()


@app.get("/health")
def health_check():
    """Return health status of the Lambda function."""
    return {"status": "healthy"}


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def handler(event: dict, context: LambdaContext) -> dict:
    """
    Main Lambda handler that processes both API Gateway and SNS events.
    """
    try:
        # Check if the event is from SNS
        if "Records" in event and event["Records"][0].get("EventSource") == "aws:sns":
            for record in event["Records"]:
                process_message(record)
            return {"statusCode": 200, "body": "SNS messages processed successfully"}

        # If not SNS, assume it's API Gateway
        return app.resolve(event, context)
    except (KeyError, ValueError) as e:
        logger.error("Error processing event structure", error=str(e))
        return {"statusCode": 400, "body": "Invalid request format"}
    except requests.RequestException as e:
        logger.error("External service request failed", error=str(e))
        return {"statusCode": 502, "body": "External service error"}
