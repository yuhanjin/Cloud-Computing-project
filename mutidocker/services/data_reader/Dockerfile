FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY grade_table.csv .
EXPOSE 5001
CMD ["python", "app.py"] 