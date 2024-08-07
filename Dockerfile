#DockerFile - Sagar
FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
ENV NAME FlaskApp
CMD ["python", "app.py"]