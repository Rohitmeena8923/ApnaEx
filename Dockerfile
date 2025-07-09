# Use official Python slim image
FROM python:3.10.11-slim

# Set work directory
WORKDIR /app

# Install required OS-level packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ffmpeg \
    libffi-dev \
    libssl-dev \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    libjpeg-dev \
    zlib1g-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Expose Flask port (for uptime pings)
EXPOSE 10000

# Start the bot using module (assuming Extractor/__init__.py has __main__ guard)
CMD ["python", "-m", "Extractor"]