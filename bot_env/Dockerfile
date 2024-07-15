# env/Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 7860

ENV GRADIO_SERVER_NAME="0.0.0.0"

# Run main.py when the container launches
ENTRYPOINT ["sh", "./env/entrypoint.sh"]