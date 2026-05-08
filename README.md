# Search Ranking Backend Platform

A lightweight backend platform designed to simulate product search, filtering, and ranking behavior commonly used in modern e-commerce and recommendation systems.

The project exposes REST APIs using FastAPI and implements custom ranking logic based on relevance, rating, and popularity signals.

---

## Core Functionalities

- Search products using keywords
- Rank results using weighted scoring logic
- Filter by category
- Filter by minimum rating
- Pagination support using limit and offset
- Fast JSON API responses
- Lightweight backend architecture
- Modular code organization

---

## Ranking Strategy

Products are ranked using a custom weighted score based on:

- Query relevance
- Product rating
- Popularity score

The final ranking score combines all three metrics to return the most relevant products first.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| JSON | Data handling |

---

## Project Structure

```text
search-ranking-backend-platform/
│
├── app/
│   ├── main.py
│   ├── search.py
│   ├── ranking.py
│   ├── database.py
│   └── models.py
│
├── data/
├── tests/
├── requirements.txt
├── Dockerfile
└── README.md

---

## Features

- FastAPI backend architecture
- Product search and ranking
- Custom relevance scoring
- Filtering and pagination
- Dockerized deployment
- GitHub Actions CI/CD
- Automated testing with Pytest
- Live deployment on Render

---

## Live API

### Swagger Docs
https://search-ranking-backend-platform.onrender.com/docs

### Search Example
https://search-ranking-backend-platform.onrender.com/search?query=laptop

---