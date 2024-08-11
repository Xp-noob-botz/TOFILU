# Use the official Python image
FROM python:3.10.8-slim-buster

# Update and upgrade packages
RUN apt-get update && apt-get upgrade -y

# Install git
RUN apt-get install -y git

# Copy requirements.txt file
COPY requirements.txt /requirements.txt

# Set the working directory
WORKDIR /

# Install Python dependencies
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

# Copy the rest of the files
COPY . /

# Start the Python script
CMD ["python3", "bot.py"]
