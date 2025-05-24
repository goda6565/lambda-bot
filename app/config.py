from pydantic_settings import BaseSettings
from app.infra.secrets_manager.get_secret import get_secret

class Settings(BaseSettings):
    slack_bot_token: str = get_secret("slack-bot-token", "ap-northeast-1")
    slack_signing_secret: str = get_secret("slack-signing-secret", "ap-northeast-1")

    class Config:
        env_file = ".env"


setting = Settings()  # pyright: ignore

if __name__ == "__main__":
    print(setting)