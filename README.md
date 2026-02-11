# 🔐 Full-Stack Login System — FastAPI & Next.js

A modern **full-stack authentication system** built using **FastAPI (backend)** and **Next.js (frontend)**, featuring secure **JWT authentication**, **password hashing**, and a clean API architecture.

---

## 🚀 Features

- 🔐 Secure user registration & login  
- 🔑 Password hashing using bcrypt  
- 🪪 JWT-based authentication  
- ⚡ FastAPI backend  
- 🌐 Next.js frontend  
- 🧱 Clean project structure  
- 🔄 CORS-enabled API for frontend integration  

---

## 🧰 Tech Stack

### Backend
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Passlib (bcrypt)**
- **JWT (python-jose)**
- **Uvicorn**

### Frontend
- **Next.js**
- **TypeScript**
- **Axios**
- **Tailwind CSS**

---

## 📁 Project Structure

```
login_system/
│
├── app/                  # FastAPI backend
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── auth.py
│
├── frontend/             # Next.js frontend
│   ├── src/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/login_system.git
cd login_system
```

---

## 🐍 Backend Setup (FastAPI)

### Create virtual environment

```bash
python -m venv .venv
```

### Activate environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run backend server

```bash
uvicorn app.main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🌐 Frontend Setup (Next.js)

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at:

```
http://localhost:3000
```

---

## 🔁 API Endpoints

| Method | Endpoint   | Description        |
|---------|-------------|-------------------|
| POST    | /register   | Register new user |
| POST    | /login      | Login user        |
| GET     | /           | Health check      |

---

## 🔐 Authentication Flow

1. User registers with username & password  
2. Password is securely hashed using bcrypt  
3. JWT token is generated on login  
4. Token is used for authenticated requests  

---

## 🛡️ Security Features

- Password hashing using **bcrypt**
- JWT access tokens
- SQL injection safe ORM queries
- CORS protection

---

## 🚀 Future Improvements

- Refresh tokens
- Role-based authentication
- Email verification
- OAuth login (Google, GitHub)
- Docker deployment
- Rate limiting & security headers

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

Built by **Your Name**

---

⭐ If you found this project useful, consider giving it a **star**!
