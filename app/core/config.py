from pydantic_settings import BaseSettings

class Settings(BaseSettings) :

    GROQ_API_KEY : str
    GEMINI_API_KEY : str
    EMBEDDING_API_URL : str 
    OCR_SPACE_API_KEY : str
    DATABASE_URL : str
    APP_NAME : str = "Study Agent"
    DEBUG : bool = True

    class Config :
        env_file = ".env"

settings = Settings()