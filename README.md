# EduPlus AI — Hack-4-Viksit Bharat 2026

## 🔹 Project Title
**EduPlus AI** — Smart Education Platform with AI-powered Doubt Solver & Risk Analytics


## 🔹 Project Overview
EduPlus AI is an AI-driven platform designed for CS students to **solve doubts step-by-step**, track **personalized learning risk**, and **practice efficiently**.  

The platform demonstrates a **scalable, cloud-ready architecture** with:  
- **FastAPI backend** for handling requests and AI integration  
- **JavaScript frontend** for interactive learning  
- **Docker deployment** for easy scalability  
- **BigQuery analytics** for risk modeling (mocked locally)  
- **Firestore storage** for tracking student scores (mocked locally)  
- **Vertex AI integration** for doubt-solving (mocked safely for hackathon demo)

This project is tailored to **Hack-4-Viksit Bharat**, showcasing **innovation + execution + real-world impact**, even without active billing.


## 🔹 Key Features

| Feature | Description |
|---------|------------|
| AI Doubt Solver | Step-by-step explanations for CS topics (DSA, Algorithms, etc.) using Vertex AI mock |
| Personalized Risk Analytics | Predicts learning gaps & risk score using scikit-learn + BigQuery mock data |
| Student Progress Tracking | Firestore integration for scores, attempts, and last activity |
| Cloud-ready Deployment | Dockerized backend ready for Cloud Run or any cloud service |
| Interactive Frontend | HTML + JS frontend calling backend endpoints |
| Mock Data Analytics | Simulated BigQuery exports and visualizations for judges |


## 🔹 Tech Stack

- **Backend:** Python, FastAPI, scikit-learn  
- **Frontend:** HTML, JavaScript (AJAX fetch)  
- **Database:** Firestore (mocked)  
- **Analytics:** BigQuery (mocked)  
- **AI:** Vertex AI (mocked)  
- **Deployment:** Docker (Cloud-ready)  
- **Monitoring & MLflow:** Markdown docs included for demonstration  


## 🔹 Folder Structure
EduPlusAI_Hackathon/ ├─ backend/ │  ├─ main.py           # FastAPI backend │  ├─ routes/           # API routes │  └─ model/            # risk_model.pkl ├─ frontend/ │  └─ index.html        # Interactive frontend ├─ Docker/ │  └─ Dockerfile        # Docker configuration ├─ data/ │  ├─ sample_students.py │  ├─ course_notes.json │  └─ bigquery_export.sql ├─ tests/ │  └─ test_api.py       # API test scripts ├─ monitoring/ │  └─ metrics.md        # Performance & analytics tracking ├─ mlflow/ │  └─ experiment.md     # Experiment tracking docs ├─ PPT/ │  └─ EduPlusAI_PPT.pdf # Presentation for judges └─ README.md            # This file


## 🔹 How to Run Locally

1. **Activate virtual environment**:

```bash
source venv/Scripts/activate   # Windows

2. Install dependencies: 
```bash
pip install -r backend/requirements.txt

3. Run Backend:
```bash 
uvicorn backend.main:app --reload

4. Open Frontend:
• Open frontend/index.html in browser
• Type a CS question → click Ask AI
• AI mock answer appears instantly

5. Docker Run 
```bash
docker build -t eduplus-ai .
docker run -p 8080:8080 eduplus-ai

• Open browser → http://127.0.0.1:8080 to see project running

🔹 Google Drive Submission
• Folder link: 
• Contains: Backend + Frontend + Docker + PPT + Mock Data + Tests + Docs

🔹 Impact Statement
EduPlus AI enables students to learn efficiently, identify weak areas, and get instant doubt resolution, simulating a real-world cloud-deployed educational AI platform.
Even without active cloud services, this setup demonstrates:
•Innovation
•Technical depth
•Scalability potential
•Hackathon-ready execution

## Author 
Alok - Solo | IIT Patna | Smart Education AI Hacakthon