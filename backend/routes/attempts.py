from fastapi import APIRouter 
from pydantic import BaseModel 
from datetime import datetime

router = APIRouter()

try: 
    from google.cloud import firestore 
    db = firestore.Client()
    FIRESTORE_ENABLED = True 
except Exception:
    db = None 
    FIRESTORE_ENABLED = False 

class Attempt(BaseModel):
    user_id: str
    topic: str
    score: int

@router.post("/save-attempt")
def save_attempt(data: Attempt):
    if not FIRESTORE_ENABLED:
        return {
            "status": "mock",
            "message": "Firestore not configured"
        }
    
db.collection("students").document(data.user_id).set(
    {
        "topic": data.topic,
        "score": data.score,
        "timestamp": datetime.utcnow(),
    },
    merge=True
)
    return {"status": "saved"},