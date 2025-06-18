# 1. Pornim de la imaginea oficială
FROM python:3.10-slim

# 2. Setăm directorul de lucru
WORKDIR /app

# 3. Instalăm toolchain-ul de build
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
     build-essential gcc g++ \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# 4. Copiem fișierul de dependencies și upgrade pip
COPY requirements.txt .
RUN pip install --upgrade pip

# 5. Instalăm dependențele
RUN pip install --no-cache-dir -r requirements.txt

# 6. Validare rapidă (asigură compatibilitate numpy↔tensorflow)
RUN python3 - <<EOF
import numpy, tensorflow
assert numpy.__version__ >= "1.26.0" and numpy.__version__ < "2.2.0", (
    f"Versiune numpy incompatibilă: {numpy.__version__}"
)
EOF

# 7. Copiem codul aplicației și expunem portul
COPY app ./app

EXPOSE 8000

# 8. Comanda default de pornire
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
