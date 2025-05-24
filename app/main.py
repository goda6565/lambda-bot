from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler

from app.infrastructure.secrets_manager.get_secret import get_secret
from app.config import setting

app = App(
    token=get_secret(f"slack-bot-token-{setting.env}", "ap-northeast-1"),
    signing_secret=get_secret(f"slack-signing-secret-{setting.env}", "ap-northeast-1"),
    process_before_response=True,
)


def lambda_handler(event, context):
    return SlackRequestHandler(app).handle(event, context)


@app.event("app_mention")
def handle_app_mention_events(event, say):
    # メッセージのタイムスタンプを取得（スレッドの親メッセージIDとして使用）
    ts = event.get("ts")
    
    # 返信メッセージを作成
    response = f"デバック: {event}"
    
    # スレッドに返信
    say(
        text=response,
        thread_ts=ts  # スレッドの親メッセージIDを指定
    )
