from fastapi import FastAPI
from backend.routes.ask_doubt import router as ask_doubt_router 
from pydantic import BaseModel
import pickle
from datetime import datetime

# GCP Imports (SAFE)
from google.cloud import firestore, bigquery

# Try Vertex AI (will safely fallback if not available)
try:
    import vertexai
    from vertexai.generative_models import GenerativeModel

    vertexai.init(
        project="YOUR_PROJECT_ID",   # <-- optional for local demo
        location="us-central1"
    )
    gen_model = GenerativeModel("gemini-1.5-flash")
    VERTEX_AVAILABLE = True
except Exception as e:
    gen_model = None
    VERTEX_AVAILABLE = False

# FastAPI App
app = FastAPI(
    title="EduPlus AI",
    description="AI-powered Smart Education Platform",
    version="1.0"
)

# Load ML Risk Model
try:
    with open("backend/model/risk_model.pkl", "rb") as f:
        risk_model = pickle.load(f)
except Exception:
    risk_model = None


# Firestore Client (SAFE)
try:
    db = firestore.Client()
except Exception:
    db = None

# Request Schemas
class DoubtRequest(BaseModel):
    question: str
    topic: str


class AttemptRequest(BaseModel):
    user_id: str
    topic: str
    score: int

# Routes
@app.get("/")
def root():
    return {
        "project": "EduPlus AI",
        "status": "running",
        "vertex_ai": True
    }
app.include_router(ask_doubt_router)

@app.post("/ask-doubt")
def ask_doubt(data: DoubtRequest):
    """
    AI-powered doubt solving.
    Falls back to mock response if Vertex AI is unavailable.
    """

    prompt = f"""
    Explain the following concept step-by-step for a Computer Science student.

    Topic: {data.topic}
    Question: {data.question}
    """

    if gen_model:
        try:
            response = gen_model.generate_content(prompt)
            answer = response.text
        except Exception:
            answer = (
                "AI response (mock): "
                "Binary Search is an efficient algorithm with time complexity O(log n)."
            )
    else:
        answer = (
            "AI response (mock): "
            "Binary Search works by repeatedly dividing the search space in half."
        )

    return {
        "topic": data.topic,
        "question": data.question,
        "answer": answer,
        "source": "Vertex AI" if gen_model else "Mock"
    }


@app.post("/save-attempt")
def save_attempt(data: AttemptRequest):
    """
    Save student quiz attempt to Firestore.
    """

    if not db:
        return {
            "status": "mock-saved",
            "message": "Firestore not configured (local demo)"
        }

    db.collection("students").document(data.user_id).set(
        {
            "scores": firestore.ArrayUnion(
                [{
                    "topic": data.topic,
                    "score": data.score,
                    "timestamp": datetime.utcnow().isoformat()
                }]
            ),
            "last_active": firestore.SERVER_TIMESTAMP
        },
        merge=True
    )

    return {
        "status": "saved",
        "user_id": data.user_id
    }


@app.get("/risk-score/{user_id}")
def get_risk_score(user_id: str):
    """
    ML-based performance risk prediction.
    """

    # Firestore unavailable → mock response
    if not db or not risk_model:
        return {
            "user_id": user_id,
            "risk_level": "Medium",
            "recommendation": "Revise DSA basics and attempt more quizzes",
            "source": "Mock"
        }

    doc = db.collection("students").document(user_id).get()

    if not doc.exists:
        return {
            "error": "User not found"
        }

    data = doc.to_dict()
    scores = [s["score"] for s in data.get("scores", [])]

    if not scores:
        avg_score = 0
    else:
        avg_score = sum(scores) / len(scores)

    try:
        risk = risk_model.predict([[avg_score]])[0]
    except Exception:
        risk = "Medium"

    return {
        "user_id": user_id,
        "average_score": avg_score,
        "risk_level": str(risk),
        "recommendation": "Practice weak topics and revise fundamentals",
        "source": "ML Model"
    }