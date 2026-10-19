
# Start with a lightweight Python image.
FROM python:3.12-slim

# Keep the application files inside /app.
WORKDIR /app

# Install Flask, which the application needs to run.
RUN pip install --no-cache-dir flask

# Copy the Python application into the image.
COPY app.py .

# Start the Flask server when the container runs.
CMD ["python", "app.py"]
