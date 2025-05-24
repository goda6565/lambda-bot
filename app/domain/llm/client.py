from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class LLMInput:
    prompt: str
    pdf_url: str
    model: str
    temperature: float


class LLMClient(ABC):
    @abstractmethod
    def generate_text(self, input: LLMInput) -> str:
        pass
