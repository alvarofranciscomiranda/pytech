# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /code
WORKDIR /code

# Copy the requirements.txt file to the working directory
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the contents of the local src directory to the working directory
COPY ./src /code

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

