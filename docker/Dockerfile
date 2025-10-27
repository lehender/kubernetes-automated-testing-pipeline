# docker/Dockerfile
FROM python:3.12-slim

# Avoid bytecode + ensure stdout/stderr unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only requirements first for layer caching
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application code
COPY app /app/app

# Expose the service port
EXPOSE 8000

# Start with gunicorn in prod mode
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app.main:app"]
