# Flask + MySQL Dockerized Application

## Overview

This project demonstrates a containerized Flask application connected to a MySQL database using Docker Compose.

The goal of the project was to practice core DevOps concepts including Docker, container networking, persistent storage, environment variables, GitHub Actions CI, and troubleshooting multi-container applications.

## Technologies Used

* Linux (WSL Ubuntu)
* Docker
* Docker Compose
* Python Flask
* MySQL 8.4
* Git
* GitHub
* GitHub Actions

## Architecture

```text
User -> localhost:8080 -> Flask Container (web) - Docker Network -> MySQL Container (db) - Docker Volume - Persistent Database Storage
```

## Features

* Multi-container architecture using Docker Compose
* Flask application running in a Docker container
* MySQL database running in a separate container
* Service-to-service communication through Docker networking
* Environment-based configuration using `.env`
* Persistent database storage using Docker volumes
* Health check endpoint (`/health`)
* Automated CI pipeline using GitHub Actions

## Environment Variables

The application uses environment variables for configuration:

```env
DB_HOST=db
DB_NAME=appdb
DB_USER=appuser
DB_PASSWORD=your_password
MYSQL_ROOT_PASSWORD=your_root_password
```

## Running Locally

### Clone Repository

```bash
git clone <repository-url>
cd project2
```

### Create Environment File

```bash
cp .env.example .env
```

Update values as required.

### Start Application

```bash
docker compose up -d --build
```

### Verify Application

```bash
curl http://localhost:8080/health
```

Expected response:

```text
OK
```

## Database Persistence

A named Docker volume is used to persist MySQL data:

```yaml
volumes:
  - mysql:/var/lib/mysql
```

This allows database data to survive container recreation.

## CI/CD

GitHub Actions automatically:

1. Checks out the repository
2. Creates a temporary `.env` file
3. Builds Docker images
4. Starts containers with Docker Compose
5. Waits for services to initialize
6. Executes a health check
7. Displays logs if a failure occurs
8. Cleans up containers

The workflow runs on:

* Push to `main`
* Pull Requests

## DevOps Concepts Demonstrated

* Docker image creation
* Docker Compose orchestration
* Container networking
* Persistent storage with volumes
* Environment variable management
* Service health checks
* CI automation with GitHub Actions
* Troubleshooting containerized applications

## Lessons Learned

During development I gained practical experience with:

* Docker networking and service discovery
* Difference between container startup and service readiness
* Managing application configuration securely
* Building CI pipelines
* Debugging containerized applications
* Working with persistent volumes
* Connecting applications to databases inside Docker networks
