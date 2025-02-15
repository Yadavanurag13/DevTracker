# devtrac - Issue Tracking System

A modern issue tracking system built with Django and Zango framework, designed for simplicity and efficiency.

## 🚀 Features

- Multi-tenant architecture with workspace isolation
- Customizable issue workflows
- Role-based access control
- Custom field support
- Advanced search and filtering

## 🛠 Tech Stack

- **Backend**: Django 4.2+, Zango Framework
- **Database**: PostgreSQL
- **Authentication**: Zango Authentication System

## 📦 Installation

### Prerequisites

#### 1. PostgreSQL Database Setup

##### Option A: Using Docker (Recommended)

```bash
# Pull PostgreSQL image
docker pull postgres

# Create persistent volume
docker volume create postgres_data

# Run PostgreSQL container
docker run --name postgres_container \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -d -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  postgres
```

#### 2. Redis Setup (Required for Celery)

##### Using Docker (Recommended)

```bash
# Pull and run Redis container
docker run --name calm_redis -d -p 6379:6379 redis
```

### Application Setup

1. Clone the repository:

```bash
git https://github.com/Yadavanurag13/devtracker.git
cd devtrac
```

2. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment:

```bash
cp .env.example .env
```

5. Update .env with your configurations:

```bash
# Database settings
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
PROJECT_NAME=devtrac
UPDATE_APPS_ON_STARTUP=True
```

6. Run migrations:

```bash
python manage.py wsmigrate_migrate issuetracker
```

## 🚀 Development

Start the development server:

```bash
python manage.py runserver
```

Access the Admin Panel at: `http://localhost:8000/platform`

Access the Application at: `http://issuetracker.com:8000/login`

## 🔧 Configuration

The application can be configured through:

- `settings.json` - Core application settings
- `policies.json` - Access control policies
- `.env` - Environment variables

## 📝 Issue Workflow

Issues can transition through the following states:

- Open
- In Progress
- Resolved
- Closed

## 🔒 Security

- Role-based access control
- Tenant data isolation
- API authentication
- CSRF protection
