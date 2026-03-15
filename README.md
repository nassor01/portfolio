# Nassoro Mohammad's Portfolio

Welcome to the personal portfolio project of Nassoro Mohammad. This project is built using Django and is designed to showcase projects, skills, and experiences with a premium dark theme and glassmorphism UI.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Local Setup](#local-setup)
3. [Running Locally](#running-locally)
4. [Deployment Steps](#deployment-steps)

---

## Prerequisites

Before starting, make sure you have the following installed on your system:
- **Python 3.x**: Ensure Python is installed and accessible via `python` or `python3` from the command line.
- **Git**: Installed and configured for version control.

---

## Local Setup

### 1. Clone the Repository
If you are pulling the code from GitHub, open your terminal and run:
```bash
git clone <your-repository-url>
cd myproject
```

### 2. Create a Virtual Environment
It's recommended to run the project in a virtual environment to manage dependencies locally.
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- **Windows**:
  ```cmd
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
Install the required Python packages from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations
Set up the initial SQLite database structure for the project:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. (Optional) Populate the Database
If you have a database population script, you can run it to load initial data like projects and skills:
```bash
python populate_db.py
```

### 7. Create a Superuser
Create an admin account to access the Django admin panel:
```bash
python manage.py createsuperuser
```
Follow the prompts to set your username, email, and password.

---

## Running Locally

### 1. Start the Development Server
```bash
python manage.py runserver
```

### 2. Access the Application
- Open your web browser and go to: `http://127.0.0.1:8000/`
- To access the admin panel, go to: `http://127.0.0.1:8000/admin/`

---

## Deployment Steps

This project is configured to be deployed on platforms like **PythonAnywhere** or **Heroku**. It uses [WhiteNoise](http://whitenoise.evans.io/) to serve static files in production.

### Phase 1: Preparing for Deployment (Locally)
1. **Ensure all changes are committed**:
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git branch -M main
   ```
2. **Push Code to GitHub**:
   ```bash
   git push -u origin main
   ```

### Phase 2: Deploying to PythonAnywhere (Example)
1. Log in to your [PythonAnywhere account](https://www.pythonanywhere.com/).
2. Open a **Bash Console** in PythonAnywhere and clone your repository:
   ```bash
   git clone <your-github-repo-url>
   ```
3. Create a **Virtual Environment** directly in the PythonAnywhere bash terminal:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 my-virtualenv
   cd <your-repo-folder>
   pip install -r requirements.txt
   ```
4. **Collect Static Files**:
   This gathers all your CSS, JS, and image files into a single directory for production serving.
   ```bash
   python manage.py collectstatic --noinput
   ```
5. **Apply Migrations**:
   Ensure the database on PythonAnywhere is up-to-date.
   ```bash
   python manage.py migrate
   ```
6. **Configure Web Tab on PythonAnywhere**:
   - Go to the **Web** tab.
   - Click **Add a new web app**.
   - Choose **Manual Configuration** (select the correct Python version).
   - Scroll down to the **Virtualenv** section and enter the path to the environment you created (e.g., `my-virtualenv`).
7. **Configure WSGI File**:
   Click on the WSGI configuration file link in the Web tab. Update it to point to your Django project. Replace the default code with:
   ```python
   import os
   import sys

   # Add your project directory to the sys.path
   path = '/home/your_username/myproject'   # Update 'your_username' and 'myproject'
   if path not in sys.path:
       sys.path.append(path)

   # Set environment variable
   os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings' # Update if your project name is different

   # Serve django via WSGI
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
8. **Reload Web App**: Hit the green **Reload** button at the top of the Web tab.
9. **Done!** Your portfolio should now be live at `https://<your_username>.pythonanywhere.com`.