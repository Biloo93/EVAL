FROM python:3.9

WORKDIR /app

COPY . /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV GROQ_API_KEY="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"

CMD ["uvicorn", "mini_groq:app", "--host", "0.0.0.0", "--port", "5000"]
