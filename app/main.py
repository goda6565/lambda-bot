import json

def handle_challenge(event_body: dict) -> dict | None:
    if event_body.get("type") == "url_verification" and "challenge" in event_body:
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"challenge": event_body["challenge"]})
        }
    return None

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
    except Exception:
        return {"statusCode": 400, "body": "invalid json"}

    # チャレンジ検証
    challenge_response = handle_challenge(body)
    if challenge_response:
        print(f"challenge_response: {challenge_response}")
        return challenge_response

    # それ以外の通常処理
    return {"statusCode": 200, "body": "Hello from lambda-bot!"}
