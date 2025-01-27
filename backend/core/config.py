import os
from dotenv import load_dotenv

from pathlib import Path
if Path('.env').exists():
    env_path = Path('.env')
else:
    env_path = Path('backend') / '.env'

print("env_path: ", env_path)
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str = "BLOG"
    PROJECT_VERSION: str = "0.1.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
settings = Settings()