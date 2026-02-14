FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (better caching)
COPY ticket/requirements.txt .

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy rest of the app
COPY ticket/ .

# Download NLTK data
RUN python - <<EOF
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
EOF

EXPOSE 8000

CMD ["python", "run_server.py"]
