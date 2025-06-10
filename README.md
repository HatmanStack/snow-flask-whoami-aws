# Snowflake Flask App - AWS Lambda Deployment

A serverless Flask application deployed on AWS Lambda with API Gateway, featuring interactive Three.js visualizations and real-time Snowflake database connectivity.

## 🚀 Live Application
**URL**: https://efgl5d8ao9.execute-api.us-west-2.amazonaws.com/Prod

## ✨ Features

### Interactive Visualizations
- **Homepage (`/`)**: Dual-layer visualization combining:
  - Vega-Lite bar chart showing name counts from Snowflake database
  - Three.js background animation with falling data sprites creating dynamic visual flow
- **HardData Page (`/HardData`)**: Immersive 3D data exploration:
  - Interactive 3D cards representing each database record
  - Drag controls for spatial rearrangement of data elements
  - Orbital camera controls for 360° data exploration

### Technical Architecture
- **Compute**: AWS Lambda (serverless Python runtime)
- **API Gateway**: RESTful HTTP endpoints with CORS support
- **Authentication**: RSA key-pair authentication with Snowflake
- **Infrastructure**: AWS SAM (Serverless Application Model)

## 🏗️ AWS Infrastructure

### Services Used
| Service | Purpose | Configuration |
|---------|---------|---------------|
| **AWS Lambda** | Serverless compute | Python 3.9 runtime, Flask handler |
| **API Gateway** | HTTP endpoints | REST API with proxy integration |
| **CloudFormation** | Infrastructure as Code | SAM template deployment |
| **CloudWatch** | Logging & monitoring | Automatic log retention |

## 📋 Prerequisites

- **AWS CLI** (v2.0+) - [Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- **AWS SAM CLI** (v1.50+) - [Installation Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- **Python 3.9+** with pip
- **Snowflake account** with database access
- **AWS account** with appropriate IAM permissions

## 🔧 Installation & Deployment

### 1. Environment Setup
```bash
# Configure AWS credentials
aws configure
# Enter: Access Key ID, Secret Access Key, Region, Output format

# Verify AWS configuration
aws sts get-caller-identity
```

### 2. Clone and Prepare
```bash
git clone https://github.com/HatmanStack/snow-flask-whoami-aws.git
cd snow-flask-whoami-aws
```

### 3. Configure Snowflake Authentication
```bash
# Generate RSA key pair (if not already done)
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -v2 aes-256-cbc -passout pass:your-passphrase
openssl rsa -in rsa_key.p8 -passin pass:your-passphrase -pubout -out rsa_key.pub

# Configure Snowflake user with public key
# In Snowflake SQL worksheet:
# ALTER USER your_service_user SET RSA_PUBLIC_KEY = '<public_key_content>';
```

### 4. Deploy to AWS
```bash
# Build the application
sam build

# Deploy with guided setup (first time)
sam deploy --guided
```

**Deployment Parameters:**
- **Stack Name**: `snow-flask-whoami-aws`
- **AWS Region**: `us-west-2` (or your preferred region)
- **Snowflake Username**: Your service account username
- **Snowflake Password**: Your private key passphrase
- **Snowflake Region**: Your Snowflake account region

### 5. Subsequent Deployments
```bash
# Quick redeploy after changes
sam build && sam deploy
```

## 💻 Local Development

### Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables
```bash
export USERNAME=your_snowflake_username
export PASSWORD=your_private_key_passphrase
export REGION=your_snowflake_region
```

### Local Testing
```bash
# Option 1: Flask development server
python -m flask run --port 8000

# Option 2: SAM local testing
sam local start-api --port 3000

# Option 3: Lambda handler testing
sam build --use-container
sam local invoke SnowFlaskFunction
```

## 📊 Monitoring & Troubleshooting

### CloudWatch Logs
```bash
# View recent logs
sam logs -n SnowFlaskFunction --stack-name snow-flask-whoami-aws --tail

# View logs for specific time period
aws logs describe-log-groups --log-group-name-prefix /aws/lambda/snow-flask-whoami
```

### Common Issues
- **Cold Start Latency**: First request may take 3-5 seconds
- **Memory Limits**: Increase in `template.yaml` if needed
- **Timeout Issues**: Adjust timeout for Snowflake queries
- **CORS Errors**: Verify API Gateway CORS configuration

## 🗂️ Project Structure
```
snow-flask-whoami-aws/
├── handler.py              # Lambda entry point
├── template.yaml           # SAM infrastructure template
├── requirements.txt        # Python dependencies
├── rsa_key.p8             # Snowflake private key
├── static/                # Frontend assets
│   ├── cards.js          # 3D card interactions
│   └── threejs-background.js # Background animations
└── templates/             # Jinja2 HTML templates
    ├── index.html        # Homepage with charts
    ├── charts.html       # Data visualization page
    ├── submit.html       # Data entry form
    └── thanks4submit.html # Confirmation page
```

## 🔐 Security Considerations

- **Snowflake Credentials**: Stored as environment variables in Lambda
- **RSA Keys**: Private key encrypted with passphrase
- **API Gateway**: CORS configured for web access
- **IAM Roles**: Minimal permissions for Lambda execution
- **VPC**: Consider VPC deployment for enhanced security

## 💰 Cost Optimization

- **Lambda**: Pay-per-request pricing (first 1M requests free monthly)
- **API Gateway**: $3.50 per million requests
- **CloudWatch**: Standard logging included in free tier
- **Estimated Monthly Cost**: <$5 for moderate usage

## 🔄 CI/CD Integration

For automated deployments, consider integrating with:
- **GitHub Actions** with AWS credentials
- **AWS CodePipeline** for full CI/CD
- **SAM CLI** in build scripts
