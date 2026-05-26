# Secure Login System

## Overview
This project is a Secure Login System developed using Python, Flask, SQLite, and bcrypt. It allows users to register and log in securely using hashed passwords while protecting against common vulnerabilities such as SQL Injection.

The application includes session management and logout functionality to ensure secure user authentication.

## Features
- User Registration
- Secure Login Authentication
- Password Hashing using bcrypt
- Input Validation
- Protection against SQL Injection
- Session Management
- Logout Feature
- Protected Dashboard Access
- SQLite Database Integration
- Optional support for Two-Factor Authentication (2FA)

## Technologies Used
- Python
- Flask
- SQLite
- Flask-Bcrypt
- HTML
- CSS

## Project Structure

Secure_Login_System/
│
├── app.py
├── database.db
├── templates/
│ ├── register.html
│ ├── login.html
│ └── dashboard.html
│
├── static/
│ └── style.css
│
├── requirements.txt
└── README.md


## Installation

Clone repository:

git clone <repository-link>

Open project folder:

cd Secure_Login_System

Install dependencies:

pip install -r requirements.txt

Run application:

python app.py

Open browser:

http://127.0.0.1:5000


## How It Works

### Registration
- User enters username and password
- Input validation checks data format
- Password is hashed using bcrypt
- User data is securely stored in database

### Login
- User enters credentials
- Password hash is verified
- Session is created after successful login

### Dashboard
- Only authenticated users can access protected pages

### Logout
- Session is destroyed securely
- User is redirected to login page

## Security Features

### Password Hashing
Passwords are never stored in plain text. bcrypt hashing secures passwords before storing them.

### SQL Injection Prevention
Parameterized SQL queries are used to prevent malicious database attacks.

### Session Security
User authentication state is maintained using Flask sessions.

## Expected Outcome
A secure login system with hashed passwords, session handling, and protection against common attacks that reduces unauthorized access and improves user account security.

## Future Improvements
- Email OTP Verification
- Two-Factor Authentication (2FA)
- Password Reset System
- Login Attempt Limiting
- CAPTCHA Integration
- Remember Me functionality

## Author
Developed as a cybersecurity and web security project.
