import requests

BASE_URL = "http://127.0.0.1:8000"

def test_ask_doubt():
    resp = requests.get(f"{BASE_URL}/ask-doubt?question=Binary+Search&topic=DSA")
    data = resp.json()
    assert "answer" in data
    print("Ask Doubt API test passed:", data["answer"])

def test_save_attempt():
    resp = requests.get(f"{BASE_URL}/save-attempt?user_id=test123&score=8&topic=DSA")
    assert resp.status_code == 200
    print("Save Attempt API test passed")

if __name__ == "__main__":
    test_ask_doubt()
    test_save_attempt()