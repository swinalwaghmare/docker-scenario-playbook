# Base image: official Python 3.11 on a slim Debian build (smaller than the full image)
FROM python:3.11-slim

# Set the working directory inside the container; later commands run from here
WORKDIR /app

# Copy only requirements.txt first so Docker can cache the dependency layer
# (it only reinstalls packages when this file changes, not on every code edit)
COPY requirements.txt .

# Install dependencies; --no-cache-dir skips pip's download cache to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project (app.py, etc.) into /app
# Do this after installing dependencies so code changes don't invalidate the layer above
COPY . .

# Document that the app listens on port 5000
# (this doesn't publish the port; you still need -p 5000:5000 when running)
EXPOSE 5000

# Command that runs when the container starts
CMD ["python", "app.py"]
# CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]