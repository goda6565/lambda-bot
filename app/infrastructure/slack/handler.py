from slack_bolt import App, Say
from slack_bolt.adapter.aws_lambda import SlackRequestHandler

from app.config import setting
from app.di.slack import init_slack_use_case
from app.domain.model.paper import Paper
from app.infrastructure.secrets_manager.get_secret import get_secret

app = App(
    token=get_secret(f"slack-bot-token-{setting.env}", "ap-northeast-1"),
    signing_secret=get_secret(f"slack-signing-secret-{setting.env}", "ap-northeast-1"),
    process_before_response=True,
)


def format_paper_for_slack(paper: Paper) -> str:
    """PaperオブジェクトをSlackメッセージ用の文字列に変換する"""
    return f"""
    *{paper.title}*

    *著者*: {", ".join(paper.authors)} 
    *カテゴリ*: {", ".join(paper.categories)}
    *公開日*: {paper.published_date}
    *URL*: {paper.url}
    *PDF*: {paper.pdf_url}

    {paper.summary}"""


def slack_handler(event, context):
    # slackは3秒以上処理が終わらないとリトライになるので、リトライが発生した場合は処理をスキップする
    if event["headers"].get("x-slack-retry-num") is not None:
        return {"statusCode": 200}
    return SlackRequestHandler(app).handle(event, context)


@app.event("app_mention")
def handle_app_mention_events(event: dict, say: Say):
    # メッセージのタイムスタンプを取得（スレッドの親メッセージIDとして使用）
    ts = event.get("ts")

    url = extract_arxiv_url(event)

    if not url or "arxiv.org/abs/" not in url:
        say(
            text="論文のURLが無効です。\n このBotはarxivの論文しか対応していません。",
            thread_ts=ts,
        )
        return

    # URLから論文IDを抽出
    paper_id = url.split("arxiv.org/abs/")[-1]
    if not paper_id:
        say(
            text="論文のURLが無効です。\n このBotはarxivの論文しか対応していません。",
            thread_ts=ts,
        )
        return

    # 返信メッセージを作成
    summarize_use_case = init_slack_use_case()
    paper = summarize_use_case.execute(paper_id)
    formatted_message = format_paper_for_slack(paper)

    # スレッドに返信
    say(
        text=formatted_message,
        thread_ts=ts,  # スレッドの親メッセージIDを指定
    )


def extract_arxiv_url(event: dict) -> str | None:
    for block in event.get("blocks", []):
        for element in block.get("elements", []):
            if element.get("type") == "rich_text_section":
                for item in element.get("elements", []):
                    if item.get("type") == "link":
                        url = item.get("url", "")
                        if "arxiv.org/abs/" in url:
                            return url
    return None
