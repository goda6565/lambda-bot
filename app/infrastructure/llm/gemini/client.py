import os
import tempfile

import requests
from google import genai
from google.genai import types

from app.domain.llm.client import LLMClient, LLMInput


class GeminiClient(LLMClient):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = genai.Client(api_key=api_key)

    def _download_pdf(self, url: str) -> str:
        """URLからPDFをダウンロードして一時ファイルとして保存する"""
        response = requests.get(url)
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(response.content)
            return temp_file.name

    def generate_text(self, input: LLMInput) -> str:
        # URLの場合、PDFをダウンロード
        if input.pdf_url.startswith(("http://", "https://")):
            temp_path = self._download_pdf(input.pdf_url)
            try:
                file = self.client.files.upload(file=temp_path)
            finally:
                # 一時ファイルを削除
                os.unlink(temp_path)
        else:
            # ローカルファイルの場合
            file = self.client.files.upload(file=input.pdf_url)

        response = self.client.models.generate_content(
            model=input.model,
            contents=[input.prompt, file],
            config=types.GenerateContentConfig(
                temperature=input.temperature,
            ),
        )

        if response.text is None:
            raise ValueError("Response content is None")
        return response.text