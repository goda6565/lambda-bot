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
        あなたは、与えられた論文を要約するAIアシスタントです。
        以下の構造に従って、各セクションの要点を簡潔かつ明確な日本語でまとめてください。

        【背景】
        【目的】
        【手法】
        【実験方法】
        【実験結果】
        【考察】
        【独自性・新規性】
        【応用可能性】
        【限界・今後の課題】

        【指示】
        - 各項目は簡潔に、かつ論文の重要な情報を正確に反映させてください。
        - 冗長な表現や曖昧な表現は避けてください。
        - 「わかりました」などの返答や、出力フォーマット以外の記述は一切しないでください。
        - 出力例がある場合は、それに従ってフォーマットと文体を統一してください。
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
