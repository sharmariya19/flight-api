from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")


class Settings:
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "postgres"
    POSTGRES_SERVER = "localhost"
    POSTGRES_PORT = 5432
    POSTGRES_DATABASE = "postgres"
    DATABSE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"


setting = Settings()
