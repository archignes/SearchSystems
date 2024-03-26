import json
import boto3
from botocore.exceptions import ReadTimeoutError

def lambda_handler(event, context):
    # Initialize the S3 client with a timeout configuration
    s3 = boto3.client('s3', config=boto3.session.Config(read_timeout=10, connect_timeout=10))

    # Specify your S3 bucket and the JSON file name
    bucket_name = 'archignes-search-systems'
    file_key = 'systems.json'

    try:
        # Fetch the JSON file from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        json_text = response['Body'].read().decode('utf-8')
        systems = json.loads(json_text)
    except ReadTimeoutError:
        return {
            'statusCode': 504,
            'body': json.dumps({'message': 'Timeout fetching systems data from S3'}),
            'headers': {'Content-Type': 'application/json'},
        }

    # Check for query parameters
    query_params = event.get('queryStringParameters', {})
    system_id = query_params.get('id')
    action = query_params.get('action')

    # If an ID is specified, filter for that system
    if system_id:
        system = next((item for item in systems if item.get('id') == system_id), None)
        result = system if system else {'message': 'System not found'}

    # If the action is to get the count, return the number of systems
    elif action == 'count':
        result = {'count': str(len(systems))}

    # If the action is to get the count, return the number of systems
    elif action == 'github-shield':
        result = {
            "schemaVersion": 1,
            "label": "Count of Systems in API",
            "message": str(len(systems)),
            "color": "blue"
        }

    # If the action is to get the systems, return the full list of systems
    elif action == 'systems':
        result = {'systems': systems}

    # Otherwise, return the status code and a note
    else:
        result = {'message': 'Welcome to the Archignes Search Systems API!'}

    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps(result),
        'headers': {'Content-Type': 'application/json'},
    }
