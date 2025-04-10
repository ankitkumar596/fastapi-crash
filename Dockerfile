FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy only the requirements file first to leverage Docker layer caching
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the FastAPI default port
EXPOSE 8000

# Start the FastAPI server using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
