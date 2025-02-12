=====
Steps
=====

A serverless AWS Lambda function that bridges SNS notifications with GitHub Actions workflows.

Features
--------
- Processes SNS messages and triggers GitHub Actions workflows
- Provides health check endpoint via API Gateway
- Uses AWS Lambda Powertools for observability
- Managed with Poetry for dependency handling

Architecture
-----------
The application consists of several components:

- **Lambda Handler**: Processes both API Gateway and SNS events
- **SNS Processing**: Parses messages and detects deployment triggers
- **GitHub Integration**: Triggers workflows via GitHub API
- **API Gateway**: Provides HTTP endpoints for health checks

Installation
-----------
.. code-block:: bash

    # Create new project
    poetry new --src "steps"

    # Install dependencies
    poetry install

    # Install development tools
    poetry add --group dev ruff

Development
----------
The project uses Poetry for dependency management and packaging:

.. code-block:: bash

    # Activate virtual environment
    poetry shell

    # Run tests
    poetry run pytest

    # Build Lambda package
    ./scripts/build.sh

Configuration
------------
Required environment variables:

.. code-block:: bash

    GITHUB_TOKEN=your_github_token
    GITHUB_OWNER=repository_owner
    GITHUB_REPO=repository_name
    WORKFLOW_NAME=workflow_to_trigger

Deployment
---------
The application is deployed using Terraform. Key components:

- Lambda function with API Gateway integration
- SNS topic subscription
- IAM roles and permissions
- Environment variables configuration

Project Structure
---------------
.. code-block:: text

    src/
      steps/
        handlers/
          main.py          # Lambda handler
        models/
          base.py         # Base data models
        services/
          github.py       # GitHub API integration
          sns.py         # SNS message processing
    terraform/           # Infrastructure as code
    scripts/            # Build and deployment scripts
    tests/             # Test suite

Contributing
-----------
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

License
-------
[Your License Here]

```sh
poetry new --src "steps"
```