# 🏥 Kidney Stone Detection System

A lightweight, real-time kidney stone detection system powered by YOLOv8 with multi-level explainability for clinical decision support.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Real-Time Detection**: 8-10ms inference on GPU, ~100ms on CPU
- **Lightweight Model**: Only 6MB (YOLOv8-nano)
- **Multi-Level Explainability**:
  - Level 1: Pixel-level attention (GradCAM)
  - Level 2: Region-level analysis
  - Level 3: Clinical prognosis
- **Clinical Analysis**: Severity assessment, treatment recommendations
- **Batch Processing**: Process multiple images simultaneously
- **Dark/Light Theme**: Modern, responsive UI

## 📁 Project Structure

```
kidney-stone-detection/
├── src/
│   └── app/
│       ├── main.py           # Flask application
│       ├── config.py         # Configuration
│       ├── models/           # Trained YOLOv8 model
│       │   └── best.pt
│       ├── static/           # CSS, JS, results
│       ├── templates/        # HTML templates
│       ├── utils/            # Explainability modules
│       └── uploads/          # Upload directory
├── docs/                     # Documentation
├── scripts/                  # Training & utility scripts
├── tests/                    # Test files
├── run.py                    # Application entry point
├── requirements.txt          # Dependencies
└── README.md
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/kidney-stone-detection.git
cd kidney-stone-detection
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python run.py
```

Open your browser at **http://localhost:5000**

## 📋 Requirements

- Python 3.8+
- PyTorch 2.0+
- CUDA (optional, for GPU acceleration)

### Core Dependencies
- Flask >= 2.0
- ultralytics >= 8.0
- torch >= 2.0
- opencv-python
- numpy
- Pillow

## 🔧 Configuration

Environment variables:
- `MODEL_PATH`: Path to custom model file
- `FLASK_DEBUG`: Enable debug mode (True/False)
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 5000)

## 📖 Documentation

- [API Documentation](docs/API_DOCUMENTATION.md)
- [Deployment Guide](docs/DEPLOYMENT_GUIDE.md)
- [Installation Guide](docs/INSTALLATION.md)

## 🧪 Testing

```bash
# Run tests
python -m pytest tests/

# Run single test
python tests/test_app.py
```

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Model Size | 6 MB |
| GPU Inference | 8-10 ms |
| CPU Inference | 80-150 ms |
| mAP@0.5 | 0.85+ |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [Flask](https://flask.palletsprojects.com/)
- Dataset from [Roboflow](https://roboflow.com/)
