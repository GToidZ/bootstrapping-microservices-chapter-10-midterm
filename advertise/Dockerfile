FROM python:3-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -R requirements.txt
COPY ./src ./src

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80" ]