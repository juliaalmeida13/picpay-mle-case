FROM python:3.11-slim

WORKDIR /app

COPY src/main.py ./src/
COPY model/model.pkl ./model/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
