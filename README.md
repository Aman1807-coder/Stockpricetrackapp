Stock Price Fetcher

A simple web application that fetches and displays stock prices using a Python backend (FastAPI) and a React frontend (Next.js). 
The app retrieves stock prices from a mock data source, stores them in a database, and displays historical data.

Technologies Used
Backend: FastAPI, SQLite, SQLAlchemy
Frontend: React.js, Next.js
API Server: Uvicorn

Setup and Run Instructions
Prerequisites
Python 3.8 or higher
Node.js (LTS version recommended)
pip (Python package manager)
npm (Node.js package manager)

Backend Setup (FastAPI)

Clone the Repository
git clone <repository_url>
cd <repository_directory>

Navigate to the Backend Directory

Create a Virtual Environment
python -m venv venv
source venv/bin/activate        # For Linux/Mac
venv\Scripts\activate           # For Windows

Install Python Dependencies:
pip install -r requirements.txt

Run the Backend Server:
uvicorn main:app --reload

The server will start at http://127.0.0.1:8000.


Frontend Setup (React + Next.js)

Navigate to the Frontend Directory
cd frontend

Install Node.js Dependencies:
npm install

Start the Development Server:
npm run dev

The frontend will start at http://localhost:3000.

Access the Frontend: Open your browser and navigate to http://localhost:3000.
Enter a stock symbol (e.g., AAPL, GOOGL) in the search box.
Click "Fetch Price" to display the latest stock price and historical data.
