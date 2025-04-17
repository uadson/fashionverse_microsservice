FROM python3.13-slim as builder

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \\
    pip install --no-cache-dir -r requirements.txt

FROM python3.13-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY ./src /app/src

EXPOSE 8000

CMD ["fastapi", "dev", "./src/main.py", "--port", "${APP_PORT:-8000}"]