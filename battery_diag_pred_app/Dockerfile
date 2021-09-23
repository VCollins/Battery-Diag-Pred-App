# Use the offical Python Image from the Docker Hub
FROM python:3.10.0

# The following 2 environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Make a new directory to place the code in.
RUN mkdir /code

# Change the working directory.
# Every command after this will be run from the /code directory
WORKDIR /code

# Copy the requirements.txt file.
COPY ./requirements.txt /code/

# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements.
RUN pip install -r requirements.txt

# Copy the rest of the code.
COPY . /code/
