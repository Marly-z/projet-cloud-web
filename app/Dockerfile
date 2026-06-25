FROM python:3.12-slim          
# mini-Linux avec Python déjà installé 
WORKDIR /app                   
# dossier de travail dans le conteneur 
COPY requirements.txt .        
# on copie d'abord la liste des dépendances 
RUN pip install --no-cache-dir -r requirements.txt 
COPY . .                       
# puis tout le code 
EXPOSE 5000                    
# port interne utilisé par l'app 
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"] 