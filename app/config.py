from pydantic import Field
from pydantic_settings import BaseSettings

from app.infra.secrets_manager.get_secret import get_secret

class Settings(BaseSettings):
    slack_bot_token: str = Field(default_factory=lambda: get_secret("slack-bot-token-prod", "ap-northeast-1"))
    slack_signing_secret: str = Field(default_factory=lambda: get_secret("slack-signing-secret-prod", "ap-northeast-1")) 

    class Config:
        env_file = ".env"


setting = Settings()  # pyright: ignore

if __name__ == "__main__":
    print(setting)