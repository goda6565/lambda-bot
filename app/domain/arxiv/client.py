from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ArxivOutput:
    paper_id: str
    title: str
    url: str
    authors: list[str]
    abstract: str
    categories: list[str]
    published_date: str


class ArxivClient(ABC):
    @abstractmethod
    def get_paper(self, paper_id: str) -> ArxivOutput:
        pass
