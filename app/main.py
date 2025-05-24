def lambda_handler(event, context):
    if "challenge" in event:
        return {
            'statusCode': 200,
            'body': event["challenge"]
        }
    

    return {
        "statusCode": 200,
        "body": "Hello from lambda-bot!"
    }