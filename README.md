# URL Shortener

A modern URL Shortener built with **FastAPI**, **SQLAlchemy**, **Redis**, and **React**. The application allows users to generate short links, track click analytics, and redirect users efficiently using a caching layer.

## Live Demo

**Frontend:** https://short.harsh-shah.me

**Backend API:** https://shortapi.harsh-shah.me

## Features

* Shorten long URLs into compact links
* Automatic redirection using unique short codes
* Click tracking and analytics
* Redis caching for faster URL lookups
* RESTful API built with FastAPI
* Interactive API documentation with Swagger UI
* React frontend with a modern user interface
* Custom domain support
* Responsive design

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Redis
* Pydantic
* Uvicorn

### Frontend

* React
* Vite
* Tailwind CSS

### Deployment

* Render (Backend & Redis)
* Vercel (Frontend)
* Namecheap (Custom Domains)

---

## Project Structure

```text
url_shortner/
│
├── backend/
│   ├── app.py
│   ├── crud.py
│   ├── db_models.py
│   ├── database_generation.py
│   ├── redis_client.py
│   └── schemas.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── requirements.txt
└── README.md
```

---

## Architecture

```text
User
 │
 ▼
React Frontend
(short.harsh-shah.me)
 │
 ▼
FastAPI Backend
(shortapi.harsh-shah.me)
 │
 ├── Redis Cache
 │
 ▼
SQLite Database
```

### URL Lookup Flow

```text
Request
   │
   ▼
Redis Cache
   │
   ├── Cache Hit
   │      ▼
   │   Redirect
   │
   └── Cache Miss
          ▼
      SQLite
          ▼
      Store in Redis
          ▼
       Redirect
```

---

## API Endpoints

### Create Short URL

```http
POST /shorten
```

Request:

```json
{
  "url": "https://example.com"
}
```

Response:

```json
{
  "shorten_url": "https://short.harsh-shah.me/abc123"
}
```

---

### Redirect URL

```http
GET /{short_code}
```

Example:

```http
GET /abc123
```

Redirects to the original URL.

---

### URL Statistics

```http
GET /stats/{short_code}
```

Response:

```json
{
  "original_url": "https://example.com",
  "short_code": "abc123",
  "clicks": 15
}
```

---

### Health Check

```http
GET /healthy
```

Response:

```json
{
  "status": "healthy"
}
```

---

## Local Setup

### Clone Repository

```bash
git clone <repository-url>
cd url_shortner
```

### Backend Setup

```bash
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
BASE_URL=http://localhost:8000
REDIS_URL=redis://localhost:6379
```

Run the backend:

```bash
uvicorn app.app:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

### Frontend Setup

```bash
cd frontend

npm install
```

Create:

```env
VITE_API_URL=http://localhost:8000
```

Run:

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## Future Improvements

* Custom aliases
* QR code generation
* PostgreSQL support
* User authentication
* Link expiration
* Advanced analytics dashboard
* Rate limiting
* Docker support
* CI/CD pipeline

---

## What I Learned

* REST API development with FastAPI
* Database design using SQLAlchemy
* Redis caching strategies
* Full-stack application development
* Deployment using Render and Vercel
* Environment variable management
* Domain configuration and DNS management

---

## Author

**Harsh Shah**
