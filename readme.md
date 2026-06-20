# 🤖 Meeting Intelligence Agent

An AI-powered assistant that automatically researches companies from upcoming calendar meetings and generates concise intelligence briefs before the meeting starts.

---

## 📌 Overview

Meeting Intelligence Agent helps professionals prepare for meetings by automatically:

- Fetching upcoming meetings from Google Calendar
- Identifying companies from attendee email domains
- Researching those companies using web intelligence
- Generating AI-powered meeting briefs
- Displaying everything in a clean dashboard

Instead of manually searching LinkedIn, Google, Crunchbase, and company websites before every call, the system prepares an actionable briefing automatically.

---

## 🚀 Features

### 📅 Google Calendar Integration

- Connects to Google Calendar API
- Fetches upcoming meetings
- Extracts attendees and meeting metadata

### 🏢 Company Identification

Automatically identifies companies from attendee email domains.

Examples:

| Email | Company |
|---------|----------|
| john@linear.app | Linear |
| priya@growthsignal.io | GrowthSignal |
| abc@notion.so | Notion |

### 🔍 Company Research Pipeline

Researches:

- Company Overview
- Recent Activity
- Funding News
- Technology Signals
- Potential Pain Points
- Suggested Talking Points

### 🤖 AI Brief Generation

Uses Gemini to generate structured meeting intelligence.

### 📊 Dashboard

Displays:

- Upcoming Meetings
- Company Information
- AI Research Briefs
- Suggested Talking Points

---

## 🏗️ Architecture

```text
Google Calendar
       │
       ▼
Meeting Fetcher
       │
       ▼
Company Extractor
       │
       ▼
Tavily Search
       │
       ▼
Gemini AI
       │
       ▼
SQLite Database
       │
       ▼
FastAPI Backend
       │
       ▼
Streamlit Dashboard
```

---

## 🛠️ Tech Stack

### Backend

- FastAPI
- SQLAlchemy
- SQLite

### AI

- Gemini 2.5 Flash

### Research

- Tavily Search API

### Frontend

- Streamlit

### Integrations

- Google Calendar API

### Deployment

- Render
- Streamlit Cloud

---

## 📂 Project Structure

```text
meeting-intelligence-agent/

├── backend/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── sync.py
│   │
│   ├── integrations/
│   │   ├── google_calendar.py
│   │   └── tavily_search.py
│   │
│   ├── services/
│   │   ├── company_extractor.py
│   │   ├── research_service.py
│   │   └── llm_service.py
│
├── frontend/
│   └── dashboard.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Setup

### Clone Repository

```bash
git clone https://github.com/your-username/meeting-intelligence-agent.git

cd meeting-intelligence-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

## 📅 Google Calendar Setup

1. Create a Google Cloud Project
2. Enable Google Calendar API
3. Create OAuth Credentials
4. Download `credentials.json`
5. Place it inside the `backend` folder

---

## ▶️ Running the Application

### Start FastAPI Backend

```bash
uvicorn backend.app:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

---

### Sync Meetings

```bash
python backend/sync.py
```

This will:

- Fetch upcoming meetings
- Extract companies
- Generate research briefs
- Store data in SQLite

---

### Start Dashboard

```bash
streamlit run frontend/dashboard.py
```

Dashboard:

```text
http://localhost:8501
```

---

## 📡 API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Get Meetings

```http
GET /meetings
```

Response:

```json
[
  {
    "title": "Intro call with Priya",
    "company": "GrowthSignal",
    "time": "2026-06-20T21:00:00",
    "brief": {}
  }
]
```

---

## 🗄️ Database Schema

### meetings

| Column | Type |
|----------|----------|
| id | Integer |
| title | String |
| company | String |
| domain | String |
| attendees | Text |
| meeting_time | String |
| brief | Text |

---

## 🤖 AI Workflow

1. Fetch meetings from Google Calendar
2. Extract attendee domains
3. Identify company
4. Research company using Tavily
5. Generate intelligence brief using Gemini
6. Save results to SQLite
7. Display in Streamlit dashboard

---

## 📈 Example Intelligence Brief

### Company Overview

High-level company description.

### Recent Activity

Funding, launches, acquisitions, partnerships.

### Tech Signals

Engineering culture and technology trends.

### Pain Points

Potential challenges faced by the company.

### Suggested Talking Points

Actionable conversation starters for meetings.

---

## 🌐 Deployment

### Backend

Deploy on Render

Start Command:

```bash
uvicorn backend.app:app --host 0.0.0.0 --port $PORT
```

---

### Frontend

Deploy on Streamlit Cloud

Add Secret:

```toml
API_URL = "https://your-render-backend.onrender.com"
```

---

## 🔮 Future Enhancements

- Background Scheduler
- Real-Time Calendar Monitoring
- CRM Integration
- Slack Integration
- PostgreSQL Support
- Multi-User Authentication
- Meeting Notifications
- Vector Database Memory
- Agentic Workflow Orchestration

---

## 🎯 Key Learnings

This project demonstrates:

- FastAPI Development
- Streamlit Development
- LLM Integration
- Prompt Engineering
- Google Calendar Integration
- External API Consumption
- Database Design
- Cloud Deployment
- End-to-End AI Product Development

---

## 👨‍💻 Author

**Satyam Gupta**

GenAI Engineer

Built as part of an AI Engineering Assignment.