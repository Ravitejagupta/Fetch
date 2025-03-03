# Step 1: Use an official Python image from the Docker Hub
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /fetchApp

# Step 3: Copy the current directory contents into the container at /app
COPY . /fetchApp

# Step 4: Install dependencies
# This assumes you have a requirements.txt file with your app's dependencies listed
RUN pip3 install -r requirements.txt

# Step 5: Expose the port that Flask will run on
EXPOSE 5000

# Step 6: Define the command to run your app
CMD ["python", "fetch.py"]
