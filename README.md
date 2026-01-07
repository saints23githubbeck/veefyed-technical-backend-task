# Images Analysis API – Technical Assessment

**Simple REST API built with FastAPI** that allows uploading images and getting mocked analysis results.

---

## Features

* **Image Upload Endpoint**: Supports JPG, JPEG, PNG; validates type and size (max 5MB)
* **Mocked Analysis Endpoint**: Returns structured JSON with skin type, detected issues, and confidence score
* Clean separation of concerns (routes, services, utils)
* Meaningful HTTP error responses for invalid requests

---

## Requirements

* Python 3.9+
* pip

---

## Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/saints23githubbeck/veefyed-technical-backend-task.git
cd veefyed-technical-backend-task

# 2. Create virtual environment (Python 3.9 recommended)
python3.9 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
uvicorn app.main:app --reload --port 5000
```

Open the interactive API docs in your browser:

```
http://127.0.0.1:5000/docs
```

---

## API Endpoints

### 1. Upload Image

**POST** `/upload`

* Accepts: JPEG / PNG
* Max size: 5MB

**Response Example:**

```json
{
  "image_id": "abc123"
}
```

---

### 2. Analyze Image

**POST** `/analyze?image_id=abc123`

* Accepts `image_id` from upload endpoint

**Response Example:**

```json
{
  "image_id": "abc123",
  "skin_type": "Oily",
  "issues": ["Hyperpigmentation"],
  "confidence": 0.87
}
```

---

## Assumptions

* Local filesystem storage is sufficient for uploaded images
* Analysis logic is **mocked** for demo purposes
* API is stateless
* Images uploaded are for testing only (not persisted in production)

---

## What Could Be Improved for Production

* Add **authentication** (API key or JWT)
* Persist image metadata in a **database**
* Use **cloud storage** (e.g., AWS S3) for scalability
* Replace mocked analysis with a **real ML/AI service**
* Add **background jobs** for heavy processing
* Add **logging and monitoring**
* Add **unit and integration tests**
* Handle **concurrent uploads and scaling**


