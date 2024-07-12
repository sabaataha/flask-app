# Use the official Python image from the Docker Hub
FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN pip install  -r requirements.txt
EXPOSE 5001
ENTRYPOINT  ["flask", "run", "--port", "5001"]
