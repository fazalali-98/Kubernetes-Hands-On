# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install Flask and Gunicorn
RUN pip install --no-cache-dir flask gunicorn

# Copy the flash-sale application
COPY app.py .

# Run the application on port 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers", "1", "--threads", "2"]