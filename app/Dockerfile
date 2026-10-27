FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && groupadd --system --gid 10001 appgroup \
    && useradd --system --uid 10001 --gid 10001 --home-dir /app appuser

COPY --chown=10001:10001 app.py .
COPY --chown=10001:10001 templates ./templates

USER 10001:10001

EXPOSE 5000

CMD ["python", "app.py"]
