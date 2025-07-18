# 🚀 Innovator Management System (IMS)

A **full-stack web application** for managing innovators, their skills, and innovation projects — designed for scalable innovation tracking within organizations.

---

## 📌 Features

- 👥 **Innovator Management** — Custom user model with email-based login.
- 📁 **Project Tracking** — Manage innovation projects from creation to completion.
- 🧠 **Skill Catalogue** — Innovators can list and update their skills.
- 🔐 **JWT Authentication** — Secure access via token-based auth.
- ⚙️ **Scalable Backend** — Built on Django + DRF, with optional GraphQL.
- 💻 **Modern Frontend** — Built with React 18 + Material UI.
- 🐳 **Containerized** — Docker-based setup for local/dev/prod.
- 🚀 **CI/CD Ready** — GitHub Actions for testing, linting, and builds.

---

## 🧰 Tech Stack

### 🔙 Backend

- **Framework:** Django 5  
- **API:** Django REST Framework (DRF)  
- **GraphQL:** (Optional) via Graphene-Django  
- **Auth:** JWT (djangorestframework-simplejwt)  
- **Database:** PostgreSQL 16  
- **Python:** 3.12  

### 🔜 Frontend

- **Framework:** React 18 (Vite)  
- **UI Library:** Material UI  
- **Forms/State:** react-hook-form  
- **HTTP Client:** axios  
- **JWT Decode:** jwt-decode  
- **Node:** 20  

### 🐳 DevOps

- **Containerization:** Docker + Docker Compose  
- **CI/CD:** GitHub Actions  
- **Lint/Format:** `ruff`, `black`, `eslint`, `prettier`  
- **Testing:** `pytest`, `vitest`  
- **Docs:** MkDocs  

---

## 📁 Project Structure

```bash
ims/
├── backend/                  # Django 5 project
│   ├── apps/                 # apps: users, projects, skills
│   ├── ims/settings/         # base, dev, prod settings
│   └── manage.py
├── frontend/                 # React 18 (Vite)
│   └── src/                  # components, pages, api, hooks
├── docker-compose.yml
└── .github/workflows/        # GitHub Actions (CI/CD)
```
---

## ⚙️ Local Development (with Docker)

# 1. Clone the repo
git clone https://github.com/TheeradetSukprem/Innovator-management.git
cd innovator-management-system

# 2. Setup environment
cp backend/.env.example backend/.env

# 3. Run all services
docker compose up --build

🌐 Frontend: http://localhost:5173

🔙 Backend API: http://localhost:8000/api/

🧪 GraphQL (optional): http://localhost:8000/graphql/
---

## 👨‍💻 My Role & Contributions

Backend Developed custom user model InnovatorUser with email login.

Integrated JWT authentication using simplejwt.

Created DRF APIs and optional GraphQL endpoint.

Frontend
Built UI components for auth and dashboard using React + MUI.

Applied responsive design for mobile/desktop compatibility.

DevOps
Wrote Dockerfiles and docker-compose for local development.

Set up GitHub Actions for CI/CD including lint/test/build.

---

## 📚 Learnings & Challenges

Area	Challenge	Resolution
JWT Refresh	Secure refresh token flow	Used custom serializer with simplejwt
Layout	Responsive design issues in React	Used MUI Grid + breakpoints
Docker	Container networking	Adjusted compose config & ports
CI/CD	YAML and dependency conflicts	Modularized workflows and isolated jobs

---

## ✅ Testing & Code Quality
Area	Toolset
Backend	pytest, pytest-django
Frontend	vitest
Formatting	ruff, black, eslint, prettier
Docs	MkDocs

🧑‍💻 Maintainer
Theeradet Sukprem
LinkedIn • Portfolio • 📫 gaxgtsk1@gmail.com