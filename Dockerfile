# Basis-Image
FROM python:3.9-slim

# Arbeitsverzeichnis setzen
WORKDIR /app

# Kopiere die Projektdateien in den Container
COPY . /app

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir requests schedule

# Starte das Python-Skript
CMD ["python", "stock.py"]