FROM python:3.12-slim

WORKDIR /schoolproject

COPY . .

RUN pip install -r requirments.txt

CMD ["python", "module_6_task_1.py"]