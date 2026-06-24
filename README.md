# WorldCupAPI 🌎🏆

A fast and simple REST API to track FIFA World Cup matches, teams, and group standings. 

This project was built to provide reliable football data. It uses a local database to store the information and an automatic script to keep the match scores updated in real-time.

## ✨ Features

- **Live Match Tracking:** A background script (`sync.py`) updates the database with live goals and match statuses.
- **Auto-Calculated Standings:** The API automatically calculates points, goals, and goal differences for the group stage.
- **Interactive Documentation:** Built-in Swagger UI to easily test the endpoints.
- **Relational Database:** Uses SQLite to safely store and connect teams and matches data.

## 💻 Technologies Used

- **Python 3**
- **FastAPI** (Web framework)
- **Uvicorn** (ASGI server)
- **SQLite** (Database)

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/quinhotheone/worldcupapi.git](https://github.com/quinhotheone/worldcupapi.git)
cd worldcupapi
```

### 2. Create a virtual environment and install dependencies
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Build the database
Run this command to create the `worldcup.db` file and populate it with the 48 teams and 104 matches:
```bash
python setup_database.py
```

### 4. Start the server
```bash
uvicorn main:app --reload
```
Now, open your browser and go to **`http://127.0.0.1:8000/docs`** to see the interactive API documentation.

### 5. Update live scores (Optional)
To update the match results, you need an API key from `football-data.org`. 
Create a `.env` file in the main folder:
```env
FOOTBALL_DATA_KEY=your_free_api_token_here
```
Then, run the sync script:
```bash
python sync.py
```

## 📍 Main Endpoints

- `GET /groups` - List all tournament groups and their teams.
- `GET /matches` - Get the list of all matches or filter them by date.
- `GET /standings` - Check the current points and group tables.

## 🔜 Next Steps (v2.0)

- Add specific statistics like cards, fouls, and corners.
- Add country flags support.
- Build a simple frontend dashboard to consume this API.