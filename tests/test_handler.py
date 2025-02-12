import json
from steps.handlers.main import handler

def test_health_check(lambda_context):
    event = {
        "httpMethod": "GET",
        "path": "/health",
        "headers": {},
        "queryStringParameters": None,
        "pathParameters": None,
        "body": None
    }
    
    response = handler(event, lambda_context)
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert body["status"] == "healthy" 