# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables to ensure Python output is sent to terminal
# and to prevent Python from writing .pyc files.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /code

# Install system dependencies (needed for psycopg2 and other tools)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . /code/

# Create a directory for the SQLite database
# This directory will be mounted to a Fly.io Volume for persistence
RUN mkdir -p /code/data

# Run collectstatic to prepare static files for WhiteNoise
# This uses the settings.py we configured earlier
RUN python manage.py collectstatic --noinput

# Expose the port Gunicorn will run on
EXPOSE 8080

# The command to start the application using Gunicorn
# Matches your "EliteSchool" project name
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "EliteSchool.wsgi:application"]
