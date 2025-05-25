import uuid


class Paper:
    def __init__(
        self,
        id: str,
        paper_id: str,
        title: str,
        url: str,
        authors: list[str],
        abstract: str,
        categories: list[str],
        pdf_url: str,
        published_date: str,
        summary: str,
    ):
        self.id = id
        self.paper_id = paper_id
        self.title = title
        self.url = url
        self.authors = authors
        self.abstract = abstract
        self.categories = categories
        self.pdf_url = pdf_url
        self.published_date = published_date
        self.summary = summary

    @classmethod
    def new_paper(
        cls,
        paper_id: str,
        title: str,
        url: str,
        authors: list[str],
        abstract: str,
        categories: list[str],
        pdf_url: str,
        published_date: str,
        summary: str,
    ) -> "Paper":
        return cls(
            id=str(uuid.uuid4()),
            paper_id=paper_id,
            title=title,
            url=url,
            authors=authors,
            abstract=abstract,
            categories=categories,
            pdf_url=pdf_url,
            published_date=published_date,
            summary=summary,
        )
