# 🔐 Full Stack Login System

A modern **full-stack authentication system** built with:

* **Backend:** FastAPI + SQLAlchemy + JWT + Bcrypt
* **Frontend:** Next.js (App Router) + TypeScript + Axios
* **Database:** SQLite (easy local dev, upgradeable to PostgreSQL / MySQL)

This project provides **secure user registration and login functionality** using industry best practices.

---

# 🚀 Features

* ✅ User Registration
* ✅ Secure Password Hashing (bcrypt)
* ✅ User Login
* ✅ JWT Authentication
* ✅ Protected Backend Routes
* ✅ Full Frontend Integration
* ✅ CORS Handling
* ✅ Clean Project Architecture

---

# 🧱 Tech Stack

## Backend

* FastAPI
* SQLAlchemy ORM
* Passlib + Bcrypt
* JWT Authentication
* SQLite (default)

## Frontend

* Next.js 16 (App Router)
* TypeScript
* Axios
* Tailwind CSS

---

# 📁 Project Structure

```
login_system/
│
├── app/                    # Backend application
│   ├── main.py
│   ├── crud.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── auth.py
│
├── frontend/               # Next.js frontend
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── package.json
│
└── README.md
```

---

# ⚙️ Backend Setup (FastAPI)

### 1️⃣ Create virtual environment

```bash
python -m venv .venv
```

### 2️⃣ Activate virtual environment

**Windows:**

```powershell
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose python-multipart
```

### 4️⃣ Run backend server

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger API docs:

```
http://127.0.0.1:8000/docs
```

---

# 🎨 Frontend Setup (Next.js)

### 1️⃣ Navigate to frontend folder

```bash
cd frontend
```

### 2️⃣ Install dependencies

```bash
npm install
```

### 3️⃣ Start development server

```bash
npm run dev
```

Frontend runs at:

```
http://localhost:3000
```

---

# 🔁 Full Development Startup

Run **two terminals**:

### Terminal 1 – Backend:

```bash
uvicorn app.main:app --reload
```

### Terminal 2 – Frontend:

```bash
cd frontend
npm run dev
```

---

# 🔐 Authentication Flow

```
Frontend → FastAPI → Database → JWT → Frontend
```

### Register

```
POST /register
```

### Login

```
POST /login
```

Returns:

```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

---

# 🛡 Security Highlights

* Passwords are **never stored in plaintext**
* Bcrypt hashing
* JWT authentication
* CORS configured
* Token expiration support

---

# 🧪 Testing

Swagger UI:

```
http://127.0.0.1:8000/docs
```

Frontend:

```
http://localhost:3000
```

---

# 🛠 Future Improvements

* 🔐 Refresh tokens
* 🧾 Email verification
* 🔁 Password reset
* 👤 Profile management
* 🔒 Role-based access control
* 🌍 Production deployment (Docker + Nginx)

---

# 📜 License

This project is licensed for **educational and personal use**.

---

