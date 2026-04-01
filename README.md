# Docker & Kubernetes Assignment

## Overview
This project demonstrates Docker containerization with a Flask application and MongoDB database using Docker Compose.

## Prerequisites
- Docker Desktop or Docker Engine
- Docker Compose
- Git
## Project Structure
.
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image configuration
├── docker-compose.yml # Multi-container configuration
└── README.md # Documentation

## How to Run

### 1. Build and Run with Docker Compose
```bash
docker-compose up -d
```
### 2. View Logs
```bash
docker-compose logs -f
```
### 3. Stop Services
```bash
docker-compose down
```

Access the Applications
Application	URL	Description
Flask App	http://localhost:5000	Main web application
MongoDB Express	http://localhost:8081	Database management UI
Step 5: Test the Application
Open http://localhost:5000

Enter a message in the input field

Click "Save" button

The message should appear in the list below

