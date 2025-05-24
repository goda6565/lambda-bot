from abc import ABC, abstractmethod

from app.domain.arxiv.client import ArxivClient
from app.domain.llm.client import LLMClient, LLMInput
from app.domain.model.paper import Paper


class SummarizeInputPort(ABC):
    @abstractmethod
    def execute(self, paper_id: str) -> Paper:
        pass


class SummarizeUseCase(SummarizeInputPort):
    def __init__(self, arxiv_client: ArxivClient, llm_client: LLMClient):
        self.arxiv_client = arxiv_client
        self.llm_client = llm_client
        self.prompt = """
        あなたは、以下に与える論文の要約を作成するAIアシスタントです。
        次の構造に従って、各セクションごとに簡潔で明確な日本語の要約を生成してください。

        出力フォーマット（各見出しを含めてください）：
        【背景】
        【目的】
        【手法】
        【実験方法】
        【実験結果】
        【考察】

        出力例を参考に、構造を必ず守ってください。冗長な表現は避け、要点を的確にまとめてください。
        """

    def execute(self, paper_id: str) -> Paper:
        paper = self.arxiv_client.get_paper(paper_id)
        pdf_url = f"https://arxiv.org/pdf/{paper_id}"
        summary = self.llm_client.generate_text(
            LLMInput(
                prompt=self.prompt,
                pdf_url=pdf_url,
                model="gemini-2.0-flash",
                temperature=0.0,
            )
        )
        published_date = paper.published_date
        return Paper.new_paper(
            paper_id=paper_id,
            title=paper.title,
            url=paper.url,
            authors=paper.authors,
            abstract=paper.abstract,
            categories=paper.categories,
            pdf_url=pdf_url,
            published_date=published_date,
            summary=summary,
        )
