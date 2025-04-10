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
   ```
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

## 🛠️ Instructions to Enable the Service:
1. **Create the service file:**
  ```bash
  sudo nano /etc/systemd/system/fastapi-app.service
  ```
2. **Reload systemd to recognize the new service:**

 ```bash
 sudo systemctl daemon-reexec
 sudo systemctl daemon-reload
```
3. **Enable the service to start on boot:**

  ```bash
  sudo systemctl enable fastapi-app.service
```
4. **Start the service:**

```bash
sudo systemctl start fastapi-app.service
```
5. **Check the status:**

```bash
 sudo systemctl status fastapi-app.service
```
