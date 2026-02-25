# Use Python 3.11 slim image for smaller size
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables for memory optimization
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    TRANSFORMERS_CACHE=/tmp \
    TORCH_HOME=/tmp \
    SENTENCE_TRANSFORMERS_HOME=/tmp

# Install system dependencies (minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies with minimal extras
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

# Copy application files
COPY . /app/

# Download NLTK data to /tmp to save space
RUN python -c "import nltk; nltk.download('punkt_tab', download_dir='/tmp/nltk_data'); nltk.download('stopwords', download_dir='/tmp/nltk_data')" && \
    mkdir -p /root/nltk_data && \
    ln -s /tmp/nltk_data /root/nltk_data

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run with minimal workers
CMD ["python", "run_server.py"]
