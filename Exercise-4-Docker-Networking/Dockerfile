
# Use a lightweight Python base image.
FROM python:3.9-slim

# Keep the application files in one directory.
WORKDIR /app

# Install the required Python packages.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application into the image.
COPY app.py .

# Document the port used by the Flask application.
EXPOSE 5001

# Start the REST API when the container launches.
CMD ["python", "app.py"]
