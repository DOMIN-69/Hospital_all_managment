<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_App-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

<br>

![Stars](https://img.shields.io/github/stars/DOMIN-69/Hospital_all_managment?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/DOMIN-69/Hospital_all_managment?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/DOMIN-69/Hospital_all_managment?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/DOMIN-69/Hospital_all_managment?style=for-the-badge)

</p>
<h1 align="center">🏥 Hospital Management System</h1>

<p align="center">
A lightweight, secure and modern Hospital Management System built with Python, Flask and MySQL.
</p>

<p align="center">
Made with ❤️ by <b>DOMIN-69</b>
</p>
 
Designed for clinics, hospitals, and healthcare organizations that need a simple web-based management solution.

---
## 📸 Preview

<p align="center">
  <img src="screenshots/dashboard.png" width="31%">
  <img src="screenshots/patients.png" width="31%">
  <img src="screenshots/appointment.png" width="31%">
</p>

## ✨ Features

- 🔐 Secure Admin Authentication
- 👨‍⚕️ Patient Management
- 📋 Appointment Management
- 💊 Medical Record Management
- 🏥 Hospital Information Settings
- 🗄️ MySQL Database Support
- ⚡ Lightweight & Fast
- 🌐 Easy VPS/cPanel Deployment

---
# 📥 Clone the Repository

If you want to download this project using Git, run:

```bash
git clone https://github.com/DOMIN-69/Hospital_all_managment.git

```

Move into the project directory:

```bash
cd Management
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Then continue with the Database Setup section below. 
# 🚀 Local Development Setup

## 📦 Download Without Git

If you don't have Git installed:

1. Click the **Code** button on the repository.
2. Select **Download ZIP**.
3. Extract the ZIP file.
4. Open the project folder.
5. Continue from the installation steps below.


## 1. Install Dependencies

Open Terminal/CMD inside the project folder and run:

```bash
pip install -r requirements.txt
```

---

## 2. Database Setup

- Open **XAMPP** or **MySQL Workbench**
- Create a database

Example:

```text
hospital_db
```

or use any database name you prefer.

Import the provided:

```
schema.sql
```

into your database.

---

## 3. Configure Database

Open:

```
config.py
```

Update your database credentials.

Example:

```python
user = "root"
password = ""
host = "localhost"
database = "hospital_db"
```

---

## 4. Run the Project

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000/
```

---

# 🌍 Deploying on VPS / Web Hosting

## Step 1

Update your production database credentials inside:

```
config.py
```

```python
user = "your_live_db_username"
password = "your_live_db_password"
host = "localhost"
database = "your_live_database"
```

---

## Step 2

Upload the complete project using:

- FTP
- File Manager
- Git Deployment

---

## Step 3 (cPanel)

Open:

```
Setup Python App
```

Create a new application.

Set:

- Application Directory → Project Folder
- Startup File → `app.py`

Install dependencies using:

```
requirements.txt
```

Finally restart the application.

---

# 🔑 Default Login

| Username | Password |
|----------|----------|
| admin | admin123 |

---

# ⚙️ Recommended After First Login

For security purposes:

- Change Admin Username
- Change Admin Password
- Update Hospital Name
- Verify settings before production use

The password field includes an **Eye Icon** to help verify your input.

---

# 📂 Project Structure

```
Hospital-Management-System/
│
├── app.py
├── config.py
├── requirements.txt
├── schema.sql
├── templates/
├── static/
└── README.md
```

---

# 🛠 Requirements

- Python 3.10+
- MySQL 8+
- Flask
- XAMPP / MySQL Workbench

---

# 📞 Support

Telegram

```
@DOMIN69ic
```

---

# 📜 License

This project is provided for educational and commercial deployment purposes.

---

# ⚠️ Notice

> **This project was originally developed as a custom solution for a client. However, the final deployment was not completed because the client decided not to proceed with the project. The source code is now shared for portfolio, educational, and demonstration purposes only.**
