# ⛽ PetroCore System
A production-ready petrol pump management backend system built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, and **JWT Authentication** with **Role-Based Access Control (RBAC)**.

---

## 📌 Project Overview

**PetroCore System** is a scalable and secure backend API designed to digitize and automate petrol pump operations.

The system provides:

* 🔐 Authentication and Authorization
* 👥 User Management
* ⛽ Fuel Management
* 💰 Sales Management
* 🧑‍🔧 Worker Profile Management
* 🗄️ Database Migration Support
* 🌍 Environment-Based Configuration
* 🧪 Automated Testing

This project follows clean architecture principles and industry-standard backend development practices.

---

## ❗ Problem Statement

Many petrol pumps still rely on manual registers, spreadsheets, or fragmented software systems to manage their daily operations. This often leads to:

* 📝 Inconsistent record keeping
* ❌ Human errors in sales entries
* 🔐 Weak access control
* 👥 Poor staff role management
* 📊 Limited business visibility
* 🗂️ Disorganized worker information

As operations grow, these challenges reduce efficiency, increase mistakes, and make auditing difficult.

---

## 💡 Solution Approach

**PetroCore System** solves these problems by providing a centralized and secure REST API platform.

Key solutions implemented:

* 🔐 JWT-based authentication
* 🛡️ Role-Based Access Control (RBAC)
* 👥 Structured user management
* ⛽ Fuel pricing and management
* 💰 Sales recording and reporting
* 🧑‍🔧 Worker profile management
* 🌍 Secure environment variables with `.env`
* 🔄 Database migrations using Alembic

This backend can be connected to web applications, mobile apps, or third-party systems.

---

## 🎯 Business Impact

With PetroCore System, petrol pump owners can:

* 📈 Improve operational accuracy
* 🔒 Enforce secure permissions
* ⚡ Reduce manual work
* 📊 Monitor business operations efficiently
* 👨‍💼 Manage employees centrally
* 🚀 Scale the software as business needs grow

---

## 🚀 Tech Stack

| Technology           | Purpose                               |
| -------------------- | ------------------------------------- |
| ⚡ FastAPI            | High-performance Python web framework |
| 🐘 PostgreSQL        | Relational database                   |
| 🧠 SQLAlchemy        | ORM for database operations           |
| 🔄 Alembic           | Database migrations                   |
| 🔐 Python-JOSE       | JWT authentication                    |
| 🛡️ Passlib + Bcrypt | Password hashing                      |
| ⚙️ Python-Dotenv     | Environment variable management       |
| 🧪 Pytest            | Automated testing                     |

---

## 🔐 Authentication & Authorization

### Authentication

* 👑 Admin Signup
* 🔓 Secure Login
* 🍪 Cookie-based JWT storage

### Role-Based Access Control (RBAC)

| Role         | Permissions                              |
| ------------ | ---------------------------------------- |
| 👑 Admin     | Full system access                       |
| 🏢 Owner     | Manage users, fuels, and worker profiles |
| 💰 SaleCheck | View all sales                           |
| 👷 Worker    | Create sales only                        |

---

## 📡 API Modules

### 🔐 Auth Operations

* `POST /signup`
* `POST /login`

### 👥 User Operations

* `GET /user/`
* `GET /user/{user_id}`
* `PATCH /user/{user_id}`
* `DELETE /user/{user_id}`

### ⛽ Fuel Operations

* `GET /fuel/`
* `POST /fuel/`
* `GET /fuel/{fuel_id}`
* `PATCH /fuel/{fuel_id}`
* `DELETE /fuel/{fuel_id}`

### 💰 Sale Operations

* `GET /sale/`
* `POST /sale/`

### 🧑‍🔧 Worker Profile Operations

* `GET /details/`
* `POST /details/`
* `GET /details/{profile_id}`
* `PATCH /details/{profile_id}`
* `DELETE /details/{profile_id}`

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

DATABASE_URL=postgresql://postgres:yourpassword@localhost/petrol_pump
SECRET_KEY=your-super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=525600

---

## 🛠️ Installation Guide

### 1️⃣ Clone the Repository

git clone [https://github.com/your-username/PetroCore-System.git](https://github.com/your-username/PetroCore-System.git)
cd PetroCore-System

### 2️⃣ Create Virtual Environment

python -m venv venv

### 3️⃣ Activate Virtual Environment

#### Windows

venv\Scripts\activate

#### Linux / macOS

source venv/bin/activate

### 4️⃣ Install Dependencies

pip install -r requirements.txt

### 5️⃣ Configure Environment Variables

Create the `.env` file as shown above.

### 6️⃣ Run Database Migrations

alembic upgrade head

### 7️⃣ Start the Application

uvicorn main:app --reload

---

## 📘 API Documentation

After starting the server, open:

* Swagger UI → `http://127.0.0.1:8000/docs`
* ReDoc → `http://127.0.0.1:8000/redoc`

---

## 🧪 Running Tests

pytest

---

## 🔒 Security Features

* 🔐 Password hashing with Bcrypt
* 🎟️ JWT-based authentication
* 🍪 Secure cookie-based token storage
* 🛡️ Role-based authorization
* 🌍 Secret management using `.env`

---

## ☁️ Deployment Ready

This project is ready to be deployed on:

* Render
* Railway
* AWS
* DigitalOcean

Recommended cloud databases:

* Neon PostgreSQL
* Supabase
* AWS RDS

---

## 🎯 Key Learning Outcomes

This project demonstrates hands-on experience with:

* REST API development
* Authentication and authorization
* Database modeling
* Alembic migrations
* Clean architecture
* Environment configuration
* Automated testing
* Deployment preparation

---

## 📈 Future Enhancements

* 📊 Dashboard analytics
* 🧾 Invoice generation
* 📥 CSV/Excel import and export
* 📧 Email notifications
* 📝 Audit logs
* 📱 Mobile application integration

---

## 👨‍💻 Author

**Ali Shaikh**
Python Backend Developer 🚀

* ⚡ FastAPI
* 🐘 PostgreSQL
* 🔐 JWT Authentication
* 🧠 SQLAlchemy
* ☁️ Deployment-Ready APIs

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

---

## 📜 License

This project is intended for educational and portfolio purposes.
