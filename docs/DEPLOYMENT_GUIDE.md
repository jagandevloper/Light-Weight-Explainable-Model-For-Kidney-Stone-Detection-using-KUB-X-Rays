# 🚀 Deployment Guide

## Kidney Stone Detection System

---

## 📋 Deployment Options

| Option | Use Case | Difficulty |
|--------|----------|------------|
| **Local Development** | Testing & Development | Easy |
| **Production Server** | Cloud Deployment | Medium |
| **Docker** | Containerized Deployment | Medium |
| **Cloud Platforms** | AWS, GCP, Azure | Advanced |

---

## 🖥️ Option 1: Local Development

### Quick Start
```bash
# Clone and navigate
git clone https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays.git
cd Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

### Access the Application
- **Local:** http://localhost:5000
- **Network:** http://YOUR_IP:5000

---

## 🌐 Option 2: Production Server (Gunicorn)

### Install Gunicorn
```bash
pip install gunicorn
```

### Run with Gunicorn
```bash
# Basic
gunicorn -w 4 -b 0.0.0.0:5000 "src.app.main:app"

# With more workers (for more traffic)
gunicorn -w 8 -b 0.0.0.0:5000 --timeout 120 "src.app.main:app"

# With access logs
gunicorn -w 4 -b 0.0.0.0:5000 --access-logfile logs/access.log "src.app.main:app"
```

### Systemd Service (Linux)
Create `/etc/systemd/system/kidney-stone.service`:

```ini
[Unit]
Description=Kidney Stone Detection Service
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/Mini-
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 "src.app.main:app"
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable kidney-stone
sudo systemctl start kidney-stone
```

---

## 🐳 Option 3: Docker Deployment

### Dockerfile
Create `Dockerfile` in project root:

```dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "run.py", "--host", "0.0.0.0"]
```

### Build and Run
```bash
# Build image
docker build -t kidney-stone-detection .

# Run container
docker run -p 5000:5000 kidney-stone-detection

# Run with GPU support
docker run --gpus all -p 5000:5000 kidney-stone-detection
```

### Docker Compose
Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./logs:/app/logs
      - ./src/app/uploads:/app/src/app/uploads
    environment:
      - FLASK_ENV=production
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

Run with:
```bash
docker-compose up -d
```

---

## ☁️ Option 4: Cloud Deployment

### AWS EC2

1. **Launch EC2 Instance**
   - AMI: Ubuntu 22.04 LTS
   - Instance Type: g4dn.xlarge (for GPU) or t3.medium (CPU only)
   - Storage: 30 GB

2. **Setup Instance**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python
sudo apt install python3.10 python3.10-venv python3-pip -y

# Clone repository
git clone https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays.git
cd Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays

# Create virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 "src.app.main:app"
```

3. **Configure Security Group**
   - Allow inbound TCP port 5000

### Google Cloud Run

1. **Create Dockerfile** (as shown above)

2. **Deploy to Cloud Run**
```bash
# Build and push to Container Registry
gcloud builds submit --tag gcr.io/PROJECT_ID/kidney-stone

# Deploy to Cloud Run
gcloud run deploy kidney-stone \
  --image gcr.io/PROJECT_ID/kidney-stone \
  --platform managed \
  --port 5000 \
  --memory 4Gi
```

### Heroku

1. **Create Procfile**
```
web: gunicorn "src.app.main:app"
```

2. **Deploy**
```bash
heroku create kidney-stone-app
git push heroku main
```

---

## 🔒 Security Considerations

### Production Checklist

- [ ] **Disable Debug Mode**
  ```python
  # In run.py or config
  DEBUG = False
  ```

- [ ] **Use HTTPS**
  - Configure SSL/TLS certificates
  - Use nginx as reverse proxy

- [ ] **Environment Variables**
  ```bash
  export SECRET_KEY="your-secure-secret-key"
  export FLASK_ENV=production
  ```

- [ ] **Rate Limiting**
  ```python
  from flask_limiter import Limiter
  limiter = Limiter(app, default_limits=["100 per hour"])
  ```

- [ ] **File Upload Validation**
  - Already implemented: 16MB limit
  - Allowed extensions: png, jpg, jpeg, bmp, tiff, gif

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        client_max_body_size 20M;
    }
}
```

---

## 📊 Performance Optimization

### GPU Optimization
- FP16 (half-precision) is enabled by default
- Batch processing for multiple images
- CUDA memory management

### CPU Optimization
- Use multiple Gunicorn workers
- Enable response caching
- Optimize image preprocessing

### Recommended Resources

| Deployment | CPU | RAM | GPU |
|------------|-----|-----|-----|
| Development | 2 cores | 4 GB | Optional |
| Production (Low) | 4 cores | 8 GB | Optional |
| Production (High) | 8 cores | 16 GB | RTX 3060+ |

---

## 📈 Monitoring

### Health Check Endpoint
```python
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'model_loaded': detector is not None}
```

### Logging
Logs are saved to `logs/` directory:
- `app.log` - Application logs
- `access.log` - Request logs (with Gunicorn)

### Metrics to Monitor
- Response time
- Memory usage
- GPU utilization
- Request count
- Error rate

---

## 🔗 Quick Reference

### Start Commands
```bash
# Development
python run.py

# Production (Gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 "src.app.main:app"

# Docker
docker run -p 5000:5000 kidney-stone-detection
```

### Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 5000 | Server port |
| `HOST` | 0.0.0.0 | Server host |
| `DEBUG` | False | Debug mode |
| `SECRET_KEY` | auto | Flask secret key |

---

## 📞 Support

For deployment issues:
- Check logs in `logs/` directory
- Open an issue on [GitHub](https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays)
- Review [Installation Guide](INSTALLATION.md)
