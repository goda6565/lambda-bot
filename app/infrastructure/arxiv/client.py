from typing import cast

import feedparser

from app.domain.arxiv.client import ArxivClient, ArxivOutput


class ArxivAPIClient(ArxivClient):
    BASE_URL = "https://export.arxiv.org/api/query"

    def get_paper(self, paper_id: str) -> ArxivOutput:
        query = f"id_list={paper_id}"
        url = f"{self.BASE_URL}?{query}"

        feed = feedparser.parse(url)
        if not feed.entries:
            raise ValueError(f"No paper found for ID: {paper_id}")

        entry = cast(feedparser.util.FeedParserDict, feed.entries[0])

        tags = entry.get("tags") or []
        categories = [str(tag["term"]) for tag in tags]

        authors = entry.get("authors") or []
        authors = [str(author.name) for author in authors]

        return ArxivOutput(
            paper_id=paper_id,
            title=str(entry.get("title")).strip(),
            url=str(entry.get("link")),
            authors=authors,
            abstract=str(entry.get("summary")),
            categories=categories,
            published_date=str(entry.get("published")),
        )


if __name__ == "__main__":
    client = ArxivAPIClient()
    print(client.get_paper("2002.03794"))
