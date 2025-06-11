# assignment_third
# Flask User Authentication App

A simple web application built with **Flask**, **MongoDB**, and **Python** that supports user registration and login with form-based frontend and backend APIs.

---

## 🚀 Features

- User Signup with email, username, and password
- User Login
- Password hashing (recommended with `werkzeug.security`)
- MongoDB backend for storing user data
- Error handling and message rendering in HTML
- Environment variable support via `.env`

---

## 🛠️ Tech Stack

- Python 3.10+
- Flask
- MongoDB
- pymongo
- requests
- python-dotenv
- Werkzeug (for password hashing)

---

## 📁 Project Structure
├── backend/
│ ├── app.py
│ ├── .env
│ └── requirements.txt
│
├── frontend/
│ ├── app.py
│ ├── .env
│ └── requirements.txt
│
└── README.md
└── .gitignore
