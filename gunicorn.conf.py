
# Define the host and port to bind to
bind = '0.0.0.0:8000'  # Bind to all network interfaces on port 8000

# Specify the number of worker processes
workers = 4  # Use 3 worker processes

# Set the maximum number of requests each worker can handle before being restarted
max_requests = 1000  # Restart workers after handling 1000 requests

# Set the maximum number of requests per worker to allow graceful shutdowns
max_requests_jitter = 100  # Add jitter to max_requests to prevent simultaneous worker restarts

# Set the timeout for graceful shutdowns
timeout = 60  # Wait up to 30 seconds for workers to finish handling requests during shutdown
