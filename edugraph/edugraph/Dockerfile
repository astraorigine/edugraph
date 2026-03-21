# Image de base: Python 3.11 sur un système léger
FROM python:3.11-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier et installer les dépendances
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier tout le projet dans le conteneur
COPY . .

# Commande par défaut au démarrage
CMD ["python", "sprint3_integration/02_integration.py"]