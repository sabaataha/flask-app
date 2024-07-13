
FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN pip install  -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=5001"]
