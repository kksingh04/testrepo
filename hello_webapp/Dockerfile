# Use a lightweight Python base image
FROM python:3.14-slim

WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]