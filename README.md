# heymix backend

This repository contains a minimal FastAPI backend scaffold.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. Copy the example environment file and adjust values as needed:
   ```bash
   cp .env.example .env
   ```

3. Run the application locally:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. Check the health endpoint at `/health/`.
