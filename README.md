# Images Analysis API – Technical Assessment

Simple REST API built with FastAPI that allows uploading images and getting mocked analysis results.

## Features
- Image upload with type & size validation (max 5MB, JPG/JPEG/PNG only)
- Mocked analysis endpoint
- Clean separation of concerns
- Meaningful HTTP error responses

## Requirements
- Python 3.9+
- pip

## Installation

```bash
# 1. Clone repository
git clone <your-repo-url>
cd veefyed-technical-backend-task

# 2. Create virtual environment (Python 3.9 recommended)
python3.9 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

run uvicorn app.main:app --reload -- 5000

open http://127.0.0.1:5000/docs

