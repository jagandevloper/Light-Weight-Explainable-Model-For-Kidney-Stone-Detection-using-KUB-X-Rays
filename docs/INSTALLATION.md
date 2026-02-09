# 📦 Installation Guide

## Kidney Stone Detection System

---

## 🚀 Quick Installation

```bash
# 1. Clone the repository
git clone https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays.git
cd Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python run.py
```

---

## 📋 System Requirements

### Minimum Requirements
| Component | Requirement |
|-----------|-------------|
| **Python** | 3.8 or higher |
| **RAM** | 8 GB |
| **Storage** | 2 GB free space |
| **OS** | Windows 10/11, macOS, Linux |

### Recommended (for GPU)
| Component | Requirement |
|-----------|-------------|
| **Python** | 3.10 or higher |
| **RAM** | 16 GB |
| **GPU** | NVIDIA RTX series |
| **CUDA** | 11.8 or higher |
| **Storage** | 5 GB free space |

---

## 🔧 Detailed Installation

### Option 1: Using pip (Simplest)

```bash
# Clone repository
git clone https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays.git
cd Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays

# Upgrade pip
pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

### Option 2: Using Virtual Environment (Recommended)

**Windows:**
```powershell
# Clone repository
git clone https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays.git
cd Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**macOS / Linux:**
```bash
# Clone repository
git clone https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays.git
cd Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Option 3: Using Conda

```bash
# Clone repository
git clone https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays.git
cd Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays

# Create conda environment
conda create -n kidney-stone python=3.10 -y
conda activate kidney-stone

# Install PyTorch with CUDA
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y

# Install other dependencies
pip install -r requirements.txt
```

---

## ✅ Verify Installation

Run these commands to verify everything is installed correctly:

```bash
# Check Python version
python --version

# Check PyTorch installation
python -c "import torch; print(f'PyTorch: {torch.__version__}')"

# Check CUDA availability
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"

# Check GPU name (if available)
python -c "import torch; print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"None\"}')"

# Check YOLOv8 installation
python -c "from ultralytics import YOLO; print('YOLOv8: OK')"

# Check Flask installation
python -c "import flask; print(f'Flask: {flask.__version__}')"
```

Expected output (with GPU):
```
PyTorch: 2.x.x
CUDA available: True
GPU: NVIDIA GeForce RTX 4050 Laptop GPU
YOLOv8: OK
Flask: 3.x.x
```

---

## 🚀 Running the Application

### Development Mode
```bash
python run.py
```

### With Custom Port
```bash
python run.py --port 8080
```

### With Debug Mode
```bash
python run.py --debug
```

### Production Mode (using Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 "src.app.main:app"
```

---

## 📁 Project Structure After Installation

```
Mini-/
├── run.py              # Entry point
├── requirements.txt    # Dependencies
├── src/
│   └── app/
│       ├── main.py     # Flask app
│       ├── models/
│       │   └── best.pt # YOLOv8 model
│       ├── templates/
│       ├── static/
│       └── utils/
├── docs/
├── scripts/
└── tests/
```

---

## ❓ Troubleshooting

### Issue: CUDA not detected
```bash
# Reinstall PyTorch with CUDA
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Issue: Module not found
```bash
# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue: Port already in use
```bash
# Use a different port
python run.py --port 8080
```

### Issue: Permission denied (Linux/macOS)
```bash
# Use sudo or change permissions
chmod +x run.py
python run.py
```

---

## 🔗 Useful Links

- **Repository:** [Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays](https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays)
- **PyTorch:** [pytorch.org](https://pytorch.org)
- **Ultralytics:** [docs.ultralytics.com](https://docs.ultralytics.com)
- **Flask:** [flask.palletsprojects.com](https://flask.palletsprojects.com)

---

## 📞 Support

If you encounter any issues, please:
1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Include your Python version, OS, and error message
