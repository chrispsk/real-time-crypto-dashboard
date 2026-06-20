# Real-Time Crypto Dashboard

A real-time cryptocurrency dashboard built with Django, Django Channels, WebSockets, Celery Beat, Redis, and Vue.js.

The application periodically requests cryptocurrency data from an external API, processes it in the background with Celery, and broadcasts live updates to connected browser clients using Django Channels and WebSockets.

## Overview

This project demonstrates a real-time data broadcasting architecture.

Instead of requiring users to manually refresh the page, the backend fetches new cryptocurrency data on a schedule and pushes updates to all connected clients automatically.

## Data Source

The project uses the CoinGecko API to fetch live cryptocurrency market data.

Endpoint used:

```text
https://api.coingecko.com/api/v3/coins/markets

## Real-Time Flow

```text
Celery Beat
     ↓
Scheduled API Request
     ↓
Celery Worker
     ↓
Django Channels
     ↓
WebSocket Broadcast
     ↓
Vue.js Frontend
     ↓
Live Crypto Dashboard
```

## Features

* Real-time cryptocurrency data updates
* Scheduled background jobs with Celery Beat
* Redis message broker
* WebSocket communication with Django Channels
* Live broadcasting to all connected clients
* Vue.js frontend rendering
* Django backend architecture
* API polling every fixed interval
* Asynchronous background processing
* Dashboard-style user interface

## Technologies Used

* Python
* Django
* Django Channels
* WebSockets
* Celery
* Celery Beat
* Redis
* Vue.js
* HTML
* CSS
* JavaScript
* SQLite

## How It Works

The application uses Celery Beat to trigger a scheduled task at a fixed interval.

That task requests cryptocurrency data from an external API. After the data is fetched, the backend forwards the result to Django Channels.

Django Channels then broadcasts the new data through WebSockets to every connected browser client.

The frontend uses Vue.js to update the dashboard dynamically without refreshing the page.

## Architecture

```text
External Crypto API
        ↑
        │
Celery Beat triggers periodic task
        │
        ↓
Celery Worker fetches API data
        │
        ↓
Redis broker coordinates background tasks
        │
        ↓
Django Channels handles WebSocket layer
        │
        ↓
Connected clients receive live updates
        │
        ↓
Vue.js updates the dashboard UI
```

## Main Components

### Django

Django is used as the main backend framework and handles the web application structure.

### Celery

Celery is used to run background tasks outside the normal request-response cycle.

### Celery Beat

Celery Beat is used to schedule periodic API requests.

### Redis

Redis is used as the message broker for Celery and can also support the real-time messaging architecture.

### Django Channels

Django Channels adds asynchronous support and WebSocket handling to the Django application.

### WebSockets

WebSockets allow the server to push live updates to the browser.

### Vue.js

Vue.js is used on the frontend to update the dashboard when new data arrives.

## Project Structure

```text
real-time-crypto-dashboard/
├── coins/
├── setari/
├── static/
├── templates/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/chrispsk/real-time-crypto-dashboard.git
cd real-time-crypto-dashboard
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Redis Setup

Redis must be running before starting Celery and the Django server.

Start Redis locally:

```bash
redis-server
```

On Windows, Redis may need to be installed through WSL, Docker, or another Redis-compatible setup.

## Database Setup

Run migrations:

```bash
python manage.py migrate
```

Create a superuser if needed:

```bash
python manage.py createsuperuser
```

## Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

Start the Celery worker.

On Linux/macOS:

```bash
celery -A setari worker -l info
```

On Windows:

```bash
celery -A setari worker -l info -P gevent
```

Start Celery Beat:

```bash
celery -A setari beat -l info
```

Open the application in the browser:

```text
http://127.0.0.1:8000/
```

## Runtime Process

When everything is running:

1. Django serves the web application.
2. Redis runs as the broker.
3. Celery worker waits for background jobs.
4. Celery Beat triggers the scheduled crypto API task.
5. The task fetches new crypto data.
6. Django Channels broadcasts the data through WebSockets.
7. Vue.js updates the frontend in real time.

## Example Use Case

A user opens the dashboard in the browser.

The browser establishes a WebSocket connection with the Django backend.

Every scheduled interval, the backend fetches updated crypto data and broadcasts it to all connected users.

The dashboard updates automatically without requiring a page refresh.
