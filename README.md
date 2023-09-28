# Who Am I : AWS

This is the AWS version of Who Am I.  It uses AWS Lambda and AWS API Gateway to build a microservice with Flask that provides an API for querying information in a Snowflake Database.  The information is displayed with interactive Vega-Lite visualizations.

## Technologies

The service is built and deployed automatically using [Zappa](https://github.com/zappa/Zappa) a python library used for deploying serverless applications to AWS Lambda.  It automatically creates a s3 bucket, execution role, API Gateway instance, and Lambda Function.  It is necessary to add your snowflake database information as an enviromental variable in the zappa.config file for the snowflake-connector-python. 

## Deployment

To run:

```
python -m venv venv

Mac/Linux:
source /venv/bin/activate

Windows:
.\venv\scripts\activate

pip install -r requirements.txt
zappa init
```

Select the defaults and add this line to zappa_settings.json replaceing `Snowflake-Region`, `Snowflake-Username`, `Snowflake-Passowrd` with your own Snowflake credentials.

```
"aws_environment_variables" : {"REGION": "<Snowflake-Region>" ,
         "PASSWORD": "<Snowflake-Password>", "USERNAME": "<Snowflake-Username>"}
```


The service is now built and deployed.  If you'd like to make changes use `zappa update`.