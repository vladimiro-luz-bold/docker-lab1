# Use Python 3.9 as the base image
FROM python:3.9  
WORKDIR /app  
# Set the working directory inside the container
COPY . .  
# Copy all application files into the container
RUN pip install flask  
# Install Flask dependency
CMD ["python", "app.py"]  
# Define command to run the app