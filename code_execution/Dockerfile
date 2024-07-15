# code_execution/Dockerfile

FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

# Copy the shell script to the working directory
COPY code_execution/execute_code.sh .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip setuptools wheel

# Make the shell script executable
RUN chmod +x execute_code.sh

# Define an entrypoint script to run Python code
ENTRYPOINT ["sh", "execute_code.sh"]