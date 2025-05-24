from app.config import setting
from app.infrastructure.arxiv.client import ArxivAPIClient
from app.infrastructure.llm.gemini.client import GeminiClient
from app.infrastructure.secrets_manager.get_secret import get_secret
from app.usecase.summary.summarize import SummarizeInputPort, SummarizeUseCase


def init_slack_use_case() -> SummarizeInputPort:
    return SummarizeUseCase(
        arxiv_client=ArxivAPIClient(),
        llm_client=GeminiClient(
            api_key=get_secret(f"gemini-api-key-{setting.env}", "ap-northeast-1")
        ),
    )
