# FinPay

A minimal demo of a payment service built with **FastAPI** and a plain HTML front‑end.

## Project layout
```
finpay/
├─ backend/            # FastAPI source
│   └─ main.py
├─ frontend/           # Simple static HTML page
│   └─ index.html
├─ requirements.txt    # Python dependencies
└─ README.md           # You are reading this
```

## Prerequisites
* Python 3.9+ installed
* `pip` available in your PATH

## Setup & run
```bash
# 1. Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # on Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the API server
uvicorn backend.main:app --reload --port 8000
```
The API will be reachable at `http://127.0.0.1:8000`.

## Front‑end
Open `frontend/index.html` in a browser (or serve it via any static server). The page talks to the API at `http://127.0.0.1:8000`. Adjust the `apiBase` variable in the script if you run the server on a different host/port.

## API endpoints
| Method | Path | Description |
|--------|------|-------------|
| GET | `/payments` | List all payments |
| POST | `/payments` | Create a new payment (JSON body) |
| GET | `/payments/{id}` | Retrieve a payment |
| DELETE | `/payments/{id}` | Delete a payment |

## License
This demo code is provided **as‑is** for educational purposes.
