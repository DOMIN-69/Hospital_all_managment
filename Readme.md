# 🏥 Hospital Management System - Setup & Deployment Guide

Welcome! This system is designed to be lightweight and easy to manage. Follow these simple steps based on your requirement.

---

## 1. Running on your Local Computer (Localhost)

**Step 1: Install Dependencies**
Open your Terminal or CMD in the project folder and run:
```bash
pip install -r requirements.txt

Step 2: Database Setup

    Open XAMPP or MySQL Workbench.

    Create a new database named hospital_db.

    Import the schema.sql file provided in this folder into the new database.

Step 3: Run the App
Run this command in your terminal:
Bash

python app.py

Open your browser and visit: http://127.0.0.1:5000/
2. Moving to a Live Server (VPS / Web Hosting)

If you decide to host this live on the internet, follow these steps:

Step 1: Database Configuration
Once your hosting provider gives you database access, update your config.py file with the new database details.

Where to change: Open config.py and replace the values:
Python

# Change these lines to your LIVE database credentials
user = 'your_live_db_username'
password = 'your_live_db_password'
host = 'localhost' # Usually stays localhost on most hosting
database = 'your_live_db_name'

Step 2: Upload Files
Upload all project files to your server (via File Manager or FTP).

Step 3: Run the Server
Most modern hosting platforms use a 'Python App' setup in cPanel.

    Go to cPanel > Setup Python App.

    Select your Python version.

    Set 'Application directory' to your project folder.

    Add requirements.txt to the configuration to install libraries.

    Click Restart to make your website live!

⚙️ Quick Settings (Admin Tips)

    Default Login: Username: admin | Password: admin123

    Security: After your first login, go to the Settings page to update your password and hospital name. The "Eye" icon in the password field helps you verify what you are typing!

For any technical support, please feel free to reach out.