FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install -r requirments.txt

EXPOSE 5000

CMD ["python", "module_6_task_1.py"]