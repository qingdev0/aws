"""
SNS service module for processing SNS messages.
"""

from aws_lambda_powertools import Logger

from steps.services.github import trigger_workflow

logger = Logger()


def process_message(record: dict) -> None:
    """
    Process a single SNS message and trigger GitHub Actions workflow if keyword pattern matches.
    """
    try:
        message = record["Sns"]["Message"]
        logger.info("Processing SNS message", message=message)

        # Check for keyword pattern (customize this condition as needed)
        if "deploy" in message.lower():
            trigger_workflow(message)

    except KeyError as e:
        logger.error("Invalid SNS message format", error=str(e))
        raise
    except ValueError as e:
        logger.error("Error processing message content", error=str(e))
        raise 