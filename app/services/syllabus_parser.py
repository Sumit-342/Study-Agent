from app.models.syllabus import Syllabus
from app.core.llm_router import llm_router

PROMPT = """You are a strict syllabus parser. Extract structure from the given text.

RULES:
1. Extract ONLY what is written in the text.
2. DO NOT invent topics.
3. Unit numbers must be integers.
4. If subject not found, use "Unknown".

SYLLABUS TEXT:
{text}

Extract the subject and all units with their topics.
"""


def parse_syllabus(text: str) -> Syllabus:
    structured_llm = llm_router.primary.with_structured_output(
        Syllabus,
        method="json_schema",
        strict=True,
    )
    result = structured_llm.invoke(PROMPT.format(text=text))
    return result