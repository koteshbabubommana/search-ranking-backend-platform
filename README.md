# Search Ranking Backend Platform

![Python](https://img.shields.io/badge/python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-green)
![Docker](https://img.shields.io/badge/docker-enabled-blue)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-success)

A scalable FastAPI backend platform for product search and ranking with filtering, pagination, custom relevance scoring, automated testing, Docker deployment, and CI/CD integration.

---

## Features

- FastAPI backend architecture
- Product search and ranking
- Custom relevance scoring
- Filtering and pagination
- REST API development
- Dockerized deployment
- GitHub Actions CI/CD pipeline
- Automated testing using Pytest
- Live deployment on Render
- Swagger API documentation

---

## Tech Stack

- Python 3.13
- FastAPI
- Uvicorn
- Pytest
- Docker
- GitHub Actions
- Render

---

## Live API

### Swagger Documentation
https://search-ranking-backend-platform.onrender.com/docs

### Search Example
https://search-ranking-backend-platform.onrender.com/search?query=laptop

---

## API Endpoints

### Home Endpoint

```http
GET /
```

### Search Endpoint

```http
GET /search?query=laptop
```

Supports:
- Query-based product search
- Pagination
- Ranking score calculation
- Relevance-based sorting

---

## Sample API Response

```json
{
  "response_time_ms": 0.03,
  "data": {
    "query": "laptop",
    "total_results": 1,
    "limit": 10,
    "offset": 0,
    "results": [
      {
        "id": 2,
        "name": "Dell XPS 13 Laptop",
        "category": "Electronics",
        "price": 1299,
        "rating": 4.6,
        "popularity": 88,
        "ranking_score": 0.952
      }
    ]
  }
}
```

---

## Project Structure

```text
search-ranking-backend-platform/

├── app/
│   ├── main.py
│   ├── search.py
│   ├── ranking.py
│   ├── database.py
│   ├── models.py
│   └── __init__.py

├── data/
│   └── products.json

├── tests/
│   └── test_search.py

├── .github/workflows/
│   └── ci.yml

├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/koteshbabubommana/search-ranking-backend-platform.git
```

Move into project folder:

```bash
cd search-ranking-backend-platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

---

## Run Tests

```bash
pytest
```

---

## Docker Setup

Build Docker image:

```bash
docker build -t search-ranking-backend-platform .
```

Run Docker container:

```bash
docker run -p 8000:8000 search-ranking-backend-platform
```

---

## CI/CD Pipeline

GitHub Actions pipeline automatically:
- Installs dependencies
- Runs tests
- Validates backend functionality
- Verifies deployment readiness

---

## Deployment

This project is deployed on Render.

Production URL:
https://search-ranking-backend-platform.onrender.com

---

## API Preview

### Swagger UI
(Add screenshot here later)

### Search API Result
(Add screenshot here later)

---

## Future Improvements

- Advanced ranking algorithms
- Elasticsearch integration
- Authentication and authorization
- Redis caching
- PostgreSQL integration
- Load testing and monitoring
- Kubernetes deployment

---

## Author

Kotesh Babu Bommana

GitHub:
https://github.com/koteshbabubommana