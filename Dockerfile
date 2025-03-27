FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY todo_backend /app/todo_backend
COPY manage.py /app/manage.py

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

EXPOSE 8001
ENTRYPOINT ["/entrypoint.sh"]
