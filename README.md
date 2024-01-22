# Flask AWS Lambda Project

This project demonstrates how to deploy a Flask application as an AWS Lambda function.

## Overview

The project includes a simple Flask application that interacts with an external API to fetch comments. The Lambda function is triggered by an API Gateway HTTP request.

## Getting Started

### Prerequisites

- Python 3.12
- AWS CLI

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/md-armaan13/ylytic-task.git

2. Create Virtual Environments
    ```bash
   cd ylytic-task
   python3 -m venv venv
   source venv/bin/activate    # On Windows, use `venv\Scripts\activate`

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
## Usage
Make HTTP requests to the API Gateway endpoint to trigger the Lambda function. The function processes the request parameters and interacts with an external API to fetch comments.
```bash
curl -X GET https://6o7w3xt9n6.execute-api.ap-south-1.amazonaws.com/search?search_author=Fredrick


