# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the .exe file into the container
COPY . .

# Expose the port the server will run on
EXPOSE 8080

# Start a basic HTTP server
CMD ["python", "-m", "http.server", "8080"]
