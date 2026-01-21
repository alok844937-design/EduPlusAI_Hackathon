from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# ---- Request schema ----
class DoubtRequest(BaseModel):
    question: str
    topic: str


def vertex_ai_answer(question: str, topic: str):
    """
    Real Vertex AI call
    Falls back safely if not configured
    """
    try:
        from vertexai.generative_models import GenerativeModel

        model = GenerativeModel("gemini-1.5-flash")
        prompt = f"""
        Explain {topic} question step-by-step for a CS student:
        {question}
        """
        response = model.generate_content(prompt)
        return response.text, "vertex-ai"

    except Exception as e:
        return (
            f"[MOCK AI]\nBinary Search ka time complexity O(log n) hota hai.\n"
            "Har step me search space half ho jata hai.",
            "mock"
        )


@router.post("/ask-doubt")
def ask_doubt(data: DoubtRequest):
    answer, source = vertex_ai_answer(data.question, data.topic)

    return {
        "topic": data.topic,
        "question": data.question,
        "answer": answer,
        "source": source
    }