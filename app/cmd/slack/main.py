from app.infrastructure.slack.handler import slack_handler


def lambda_entrypoint(event, context):
    return slack_handler(event, context)
