FROM python:3.12-slim

WORKDIR /schoolproject

COPY . .

RUN pip install -r requirements.txt

expose 5000

CMD ["python", "module_6_task_1.py"]