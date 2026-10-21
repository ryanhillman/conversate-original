# Conversate - 2020

<p align="center">
  <img src="https://img.shields.io/badge/Security-Auth0-EB5424" />
  <img src="https://img.shields.io/badge/Backend-Flask-000000?logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Frontend-Vue.js-42B883?logo=vue.js&logoColor=white" />
</p>

Conversate is a full-stack web application for learning basic Italian. 

[Visit modernized version of Conversate here.](https://github.com/ryanhillman/conversate-modernization)

It was originally designed as a capstone group project and is incomplete.

Thank you to everyone involved.

---

## Tech Stack

**Backend**
- Python 3.7
- Flask
- SQLAlchemy
- PostgreSQL
- Alembic
- Gunicorn

**Frontend**
- Vue 2
- Vue Router
- Axios
- Sass

**Authentication**
- Auth0

---

## How to Run

Requires Python 3.7, Node 10, PostgreSQL, and Docker.

### PostgreSQL

```bash
psql -U postgres -c "CREATE DATABASE conversate;"
psql -U postgres -c "CREATE ROLE conversate LOGIN PASSWORD 'conversate';"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE conversate TO conversate;"
```

### Backend

```bash
cd backend
py -3.7 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install "Werkzeug==0.16.1" "MarkupSafe==1.1.1" "click==7.1.2" "itsdangerous==1.1.0"
```

Create a `.env` file in `backend/` with:
```
DATABASE_URL=postgresql://conversate:conversate@127.0.0.1:5432/conversate
DEBUG=True
```

```bash
python manage.py db upgrade
python run.py
```

### Frontend

```bash
cd front-end
docker run -it --rm -p 3000:3000 -v "${PWD}:/app" -w /app node:10-alpine sh -c "npm install regenerator-runtime && npm install && npx vue-cli-service serve --host 0.0.0.0 --port 3000"
```

### Auth0

Set `domain`/`clientId` in `front-end/auth_config.json` for your own Auth0 Single Page Application, with `http://localhost:3000` added to its Allowed Callback URLs, Logout URLs, and Web Origins.

---

## Screenshot

![App Screenshot](./docs/screenshot.png)