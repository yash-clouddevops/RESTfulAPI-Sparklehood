# AI Safety Incident Log API

A simple **RESTful API** built with **Flask** and **Flask-SQLAlchemy** to log and manage hypothetical AI safety incidents.

Repository Link: [RESTfulAPI-Sparklehood](https://github.com/yash-clouddevops/RESTfulAPI-Sparklehood.git)

---

## 🛠 Features
- Log new AI safety incidents.
- View all logged incidents.
- View a specific incident by ID.
- Delete an incident by ID.
- Basic validation and error handling.
- Uses lightweight **SQLite** database (`data.db`).

---

## ⚡ Technology Stack
- **Python 3**
- **Flask 3.1**
- **Flask-SQLAlchemy 3.1**
- **SQLite**

---

## 📦 Project Structure
```
incidents.py         # Main application file
requirements.txt     # Python dependencies
data.db              # SQLite database (created automatically on first run)
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yash-clouddevops/RESTfulAPI-Sparklehood.git
cd RESTfulAPI-Sparklehood
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python incidents.py
```
The server will start at:
> http://127.0.0.1:5000

---

## 🌐 API Endpoints

### `GET /incidents`
- Retrieve all incidents.
- **Response**: `200 OK`
```json
[
  {
    "id": 1,
    "title": "Example Incident",
    "description": "An example of AI incident.",
    "severity": "High",
    "reported_at": "2025-04-26T12:00:00"
  }
]
```

---

### `POST /incidents`
- Create a new incident.
- **Request Body**:
```json
{
  "title": "Unexpected AI Behavior",
  "description": "The AI system recommended harmful actions to users.",
  "severity": "High"
}
```
- **Response**: `201 Created`
```json
{
  "id": 2,
  "title": "Unexpected AI Behavior",
  "description": "The AI system recommended harmful actions to users.",
  "severity": "High",
  "reported_at": "2025-04-26T12:30:00"
}
```
- **Note**: Severity must be one of: `Low`, `Medium`, `High`.

---

### `GET /incidents/<id>`
- Retrieve a specific incident by ID.
- **Example**: `GET /incidents/1`
- **Response**: `200 OK`
```json
{
  "id": 1,
  "title": "Example Incident",
  "description": "An example of AI incident.",
  "severity": "High",
  "reported_at": "2025-04-26T12:00:00"
}
```
- **Error**: `404 Not Found` if incident does not exist.

---

### `DELETE /incidents/<id>`
- Delete an incident by ID.
- **Example**: `DELETE /incidents/1`
- **Response**: `204 No Content`
- **Error**: `404 Not Found` if incident does not exist.

---

## 🔥 Quick Testing (Using cURL)

### Create a New Incident
```bash
curl -X POST http://127.0.0.1:5000/incidents -H "Content-Type: application/json" -d '{"title": "AI Bias Detected", "description": "Detected bias in recruitment AI.", "severity": "Medium"}'
```

### List All Incidents
```bash
curl http://127.0.0.1:5000/incidents
```

### Get a Specific Incident
```bash
curl http://127.0.0.1:5000/incidents/1
```

### Delete an Incident
```bash
curl -X DELETE http://127.0.0.1:5000/incidents/1
```

---

## ⚠️ Notes
- Database file (`data.db`) is created automatically on first run.
- Basic validations are in place (missing fields or invalid severity).
- This project is ideal for learning RESTful APIs with Flask.

---

## 👨‍💻 Author
**Yash - Cloud DevOps Engineer**  
GitHub: [@yash-clouddevops](https://github.com/yash-clouddevops)
