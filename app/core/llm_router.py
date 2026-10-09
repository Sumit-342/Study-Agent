from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

class LLMRouter :
    def __init__(self):
        self.primary = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model="openai/gpt-oss-120b",
            temperature=0.3
        )

        self.fallback = ChatGoogleGenerativeAI(
            api_key = settings.GEMINI_API_KEY,
            model = "gemini-2.5-flash",
            temperature = 0.3
        )

    def invoke(self , messages) :
        try :
            return self.primary.invoke(messages)

        except Exception as e :
            print("Groq Failed {e} Switching to Gemini")
            return self.fallback.invoke(messages)


llm_router = LLMRouter()