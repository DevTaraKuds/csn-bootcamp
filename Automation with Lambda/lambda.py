import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Extract the key (file path)
    s3_info = event['Records'][0]['s3']
    key = s3_info['object']['key']
    
    # Get folder name (first part of the key)
    folder = key.split('/')[0] if '/' in key else 'No folder'
    
    logger.info(f"New file uploaded to folder: {folder}")
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Folder: {folder}")
    }
