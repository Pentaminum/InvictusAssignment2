# Company Profile Manager & Input Validator

This project is a lightweight full-stack web application for managing company profile data and validating user inputs.

## Project Structure

```
backend/
frontend/
```

## Running the application
Open two terminals: one for the backend and one for the frontend.

### Backend(FastAPI)

```
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment (choose one)
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Run backend server
uvicorn app.main:app --reload
```
Backend runs at: http://localhost:8000


### Frontend(React + Vite)
```
cd frontend

# Install dependencies
npm install

# Run frontend development server
npm run dev
```
Frontend runs at: http://localhost:5173

