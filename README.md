# FastAPI Crash Project

This document outlines the initial setup and Git configuration steps for the FastAPI Crash project.

## 🛠️ Project Setup

1. **Create the project directory:**
   ```bash
   mkdir fastapi-crash
   cd fastapi-crash/
2. **Set up a Python virtual environment:**
3. ```bash
   python3 -m venv .venv
   source .venv/bin/activate
4. **Capture the current dependencies (if any):**
   ```bash
   pip freeze > requirements.txt
5. **Run the application:**
   ```bash
    uvicorn main:app --reload
   
## 🛠️ Git Setup
1. ** Clone the repository:**
   ``` bash
   git clone -b main https://github.com/ankitkumar596/fastapi-crash/
   cd fastapi-crash
   source .venv/bin/activate
   uvicorn main:app --reload

🛠️ Instructions to Enable the Service:
Create the service file:

bash
Copy
Edit
sudo nano /etc/systemd/system/fastapi-app.service
Paste the above content into the file and save (Ctrl+O, Enter, then Ctrl+X).

Reload systemd to recognize the new service:

bash
Copy
Edit
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
Enable the service to start on boot:

bash
Copy
Edit
sudo systemctl enable fastapi-app.service
Start the service:

bash
Copy
Edit
sudo systemctl start fastapi-app.service
Check the status:

bash
Copy
Edit
sudo systemctl status fastapi-app.service