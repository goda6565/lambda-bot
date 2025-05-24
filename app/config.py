from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    slack_bot_token: str = ""
    slack_signing_secret: str = ""

    class Config:
        env_file = ".env"


setting = Settings()  # pyright: ignore

if __name__ == "__main__":
    print(setting)