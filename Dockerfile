# Utiliser une image Python comme base
FROM python:3.9.21

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Installer Jupyter et ipykernel pour les notebooks
RUN pip install jupyter ipykernel

# Assurer que le conteneur peut fonctionner comme un kernel
RUN python -m ipykernel install --name "docker_env" --display-name "Python (Docker)"

# Exposer le port pour le serveur Jupyter (optionnel)
EXPOSE 8888

# Garde le conteneur actif pour le développement
CMD ["tail", "-f", "/dev/null"]

