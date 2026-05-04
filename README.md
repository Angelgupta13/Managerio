# Managerio - AI-Powered Employee Wellbeing Platform

## 🌟 Project Overview

Managerio is a comprehensive full-stack web application designed to detect employee burnout before it manifests as attrition. Built with modern technologies including Next.js 16 and FastAPI, it provides actionable insights for HR managers and team leads through three specialized analysis engines.

## 🎯 Problem Statement

Employee burnout has become a critical issue:
- **76%** of employees experience burnout (Harvard Business Review)
- **$500 Billion** annual cost to US organizations
- **6 months** average detection time (at exit interview)
- **$150,000 - $300,000** cost per engineer resignation

## 🏗️ Tech Stack

### Frontend
- **Next.js 16** - React framework with App Router
- **React 19** - UI Library
- **TypeScript 5** - Type safety
- **Tailwind CSS v4** - Styling
- **Recharts & D3.js** - Data visualization
- **Supabase Auth** - Authentication

### Backend
- **FastAPI 0.109** - Python async web framework
- **Python 3.12** - Runtime
- **SQLAlchemy** - ORM
- **Gemini 2.5 Flash** - LLM for AI features
- **NetworkX** - Graph analysis
- **SciPy** - Statistical calculations

### Database
- **Supabase** - PostgreSQL + Authentication
- **Two-Vault Architecture** - Privacy-first design

## ✨ Key Features

### Three Analysis Engines
1. **Safety Valve** - Burnout detection using velocity, belongingness, and circadian entropy
2. **Talent Scout** - Network analysis to find structurally critical "hidden gems"
3. **Culture Thermometer** - Team health monitoring using SIR epidemiological model

### AI-Powered Chat (Ask Sentinel)
- 3-agent orchestrator with intelligent routing
- Server-Sent Events (SSE) streaming
- Tool integrations via Composio MCP

### Role-Based Access Control
- 52-permission RBAC system
- Three roles: Employee, Manager, Admin
- GDPR-compliant consent management

## 🚀 Quick Start

### Prerequisites
- Node.js 20+
- Python 3.12+
- Supabase account

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python -m uvicorn app.main:app --reload --port 8000
```

### Database Setup
1. Create a Supabase project at https://supabase.com
2. Update `DATABASE_URL` in `backend/.env`
3. Run: `python setup_db.py`
4. Seed demo data: `python -m scripts.seed_fresh`

## 👤 Demo Credentials

| Email | Password | Role |
|-------|----------|------|
| admin@acme.com | Demo123! | Admin |
| eng.manager@acme.com | Demo123! | Manager |
| dev1@acme.com | Demo123! | Employee |

## 📁 Project Structure

```
Managerio/
├── frontend/           # Next.js 16 Frontend
│   ├── app/           # App Router pages
│   ├── components/    # React components
│   ├── lib/           # API client, utilities
│   └── hooks/         # Custom React hooks
│
├── backend/           # FastAPI Backend
│   ├── app/
│   │   ├── api/      # API endpoints
│   │   ├── services/ # Business logic
│   │   └── models/   # Database models
│   └── scripts/       # Seed scripts
│
└── README.md          # This file
```

## 📊 Features Implemented

- ✅ User Authentication with JWT
- ✅ Role-based Dashboards (Employee, Manager, Admin)
- ✅ Safety Valve Engine - Burnout detection
- ✅ Talent Scout Engine - Network analysis
- ✅ Culture Thermometer - Team health
- ✅ 3-Agent AI Chat with SSE streaming
- ✅ 52-permission RBAC system
- ✅ Data Visualization (Recharts, D3.js)
- ✅ GDPR Consent Management

## 📝 Project Report

See `PROJECT_REPORT_V2.html` for detailed documentation (6-8 pages).

## 👥 Team

- [Your Name] - [Roll Number]

## 📜 License

This project is for academic submission purposes.

---

**Bharati Vidyapeeth's College of Engineering, New Delhi**  
**Web Technologies Lab - PBL Mini Project**  
**Faculty: Mohit Tiwari**