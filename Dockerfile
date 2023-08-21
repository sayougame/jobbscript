# Använd en officiell Python-runtime som en förälder-bild
FROM python:3.7-slim

# Sätt arbetskatalogen i behållaren till /app
WORKDIR /app

# Lägg till aktuell kataloginnehåll till arbetsplatsen i behållaren
ADD . /app

# Installera alla nödvändiga paket specificerade i requirements.txt
RUN pip install --no-cache-dir flask twilio

# Gör port 5000 tillgänglig för världen utanför denna behållare
EXPOSE 5000

# Kör script.py när behållaren startar
CMD ["python", "script.py"]
