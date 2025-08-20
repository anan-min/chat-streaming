FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y build-essential

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port if you run FastAPI (change if needed)
EXPOSE 8000

# Default command (change main.py if needed)
CMD ["python", "main.py"]