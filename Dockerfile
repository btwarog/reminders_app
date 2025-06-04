FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Environment variables will be provided at runtime
ENV BOT_TOKEN=""
ENV CHAT_ID=""

# Run the application with unbuffered output
CMD ["python", "-u", "app.py"]
