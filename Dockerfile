# Use Python version 3.9
FROM python:3.9-slim

# Set up an environment variables 
ENV PROJECT_DIR /rest_api
ENV FLASK_ENV development
ENV FLASK_APP app.py

# Set the project dir as the working directory (like we 'cd' into that dir in
# the container)
WORKDIR ${PROJECT_DIR}

# Copy all of the local files to the project directory
COPY ./rest_api ${PROJECT_DIR}/

# Install all the dependencies
RUN apt-get update -y
RUN apt-get install -y build-essential
RUN apt-get install -y libpq-dev
RUN pip install -r requirements.txt

# Run the application, on port 80
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "80"]

