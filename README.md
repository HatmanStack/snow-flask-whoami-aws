# Snowflake Flask App - AWS Deployment

This repository contains a Flask application that displays database information from a Snowflake database, deployed on AWS Lambda with API Gateway.

## Enhanced Visualizations

### Homepage (/)
The homepage features a dual-layer visualization:
1. **Vega-Lite Chart**: A bar chart showing name counts from the Snowflake database
2. **Three.js Background Animation**: A dynamic background with falling data sprites representing database entries. The animation creates a sense of data flow and adds visual interest to the page.

### HardData Page (/HardData)
The HardData page has been completely overhauled with an interactive 3D visualization:
1. **Interactive 3D Cards**: Each database record is represented as a 3D card in a Three.js scene
2. **Drag Controls**: Users can click and drag cards to rearrange them in 3D space
3. **Orbit Controls**: Users can rotate and zoom the camera to explore the data from different angles

## Deployment

This application is deployed on AWS using:
- **AWS Lambda**: Serverless compute service
- **API Gateway**: HTTP endpoint for the Lambda function
- **AWS SAM**: Infrastructure as Code for deployment

### Prerequisites
- AWS CLI
- AWS SAM CLI
- Python 3.9+
- Snowflake account with proper credentials

### Deployment Steps
1. Configure your AWS credentials:
   ```
   aws configure
   ```

2. Deploy using SAM:
   ```
   sam build
   sam deploy --guided
   ```

3. During the guided deployment, you'll need to provide:
   - Stack name
   - AWS Region
   - Snowflake username
   - Snowflake password
   - Snowflake region

## Local Development

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set environment variables:
   ```
   export USERNAME=your_snowflake_username
   export PASSWORD=your_snowflake_password
   export REGION=your_snowflake_region
   ```

3. Run locally:
   ```
   python -m flask run
   ```

## Live Demo
The application is deployed at: https://akxv1pi5yc.execute-api.us-west-1.amazonaws.com/dev
