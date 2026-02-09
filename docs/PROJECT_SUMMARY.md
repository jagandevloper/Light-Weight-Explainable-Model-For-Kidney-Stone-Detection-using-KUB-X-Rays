# 🏥 Kidney Stone Detection System - Project Summary

## 📋 Overview

A lightweight, real-time kidney stone detection system powered by **YOLOv8** with multi-level explainability features. Built with Flask for web deployment and optimized for both CPU and GPU inference.

**Repository:** [Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays](https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays.git)

---

## ✅ Key Features

### 🔬 Detection Capabilities
- **Real-time Detection**: Fast inference on medical images
- **YOLOv8 Nano Model**: Lightweight (~6MB) with excellent accuracy
- **GPU Acceleration**: CUDA support with FP16 half-precision
- **Adjustable Confidence**: Threshold slider (0.1 - 0.9)

### 🧠 Multi-Level Explainability
- **Pixel-Level (GradCAM)**: Heatmap visualization of model attention
- **Region-Level (Attention Maps)**: Anatomical region analysis
- **Image-Level (Clinical Prognosis)**: Risk assessment and recommendations

### 🎨 Modern Web Interface
- **Glassmorphism UI**: Clean, modern design
- **Dark/Light Theme**: Toggle between themes
- **Responsive Layout**: Works on all devices
- **Drag & Drop Upload**: Easy image upload

---

## 📁 Project Structure

```
Mini-/
├── run.py                  # 🚀 Main entry point
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
│
├── src/                    # Source code
│   └── app/
│       ├── main.py         # Flask application
│       ├── config.py       # Configuration settings
│       ├── models/
│       │   └── best.pt     # Trained YOLOv8 model
│       ├── templates/
│       │   └── index.html  # Web interface
│       ├── static/
│       │   ├── css/        # Stylesheets
│       │   └── results/    # Detection results
│       ├── uploads/        # Uploaded images
│       └── utils/
│           ├── explainability.py
│           ├── advanced_explainability.py
│           └── clinical_relevance.py
│
├── docs/                   # Documentation
│   ├── PROJECT_SUMMARY.md
│   ├── API_DOCUMENTATION.md
│   ├── INSTALLATION.md
│   └── DEPLOYMENT_GUIDE.md
│
├── scripts/                # Utility scripts
│   ├── train.py            # Model training
│   ├── evaluate.py         # Model evaluation
│   ├── inference.py        # Batch inference
│   ├── real_time.py        # Real-time detection
│   └── explainability.py   # Explainability tools
│
└── tests/                  # Test files
    ├── test_app.py
    └── simple_test.py
```

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays.git
cd Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

Open **http://localhost:5000** in your browser.

---

## 📊 Performance Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| **Model Size** | ~6 MB | YOLOv8 Nano |
| **GPU Inference** | 8-15ms | RTX 4050 with FP16 |
| **CPU Inference** | 80-150ms | Depends on CPU |
| **mAP@0.5** | 44.7% | Medical detection |
| **Precision** | 67.1% | Low false positives |
| **Recall** | 48.3% | Detection rate |

---

## 🔧 Technical Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Flask 3.x |
| **ML Framework** | PyTorch 2.x |
| **Object Detection** | Ultralytics YOLOv8 |
| **Image Processing** | OpenCV, NumPy |
| **Frontend** | HTML5, CSS3, JavaScript |
| **GPU Support** | CUDA 11.x+ |

---

## 🎯 Severity Scoring Algorithm

```
Severity Score = Size Score + Confidence Score + Count Score
                 (50 points)    (30 points)       (20 points)

Risk Levels:
├── Low Risk:      < 40 points
├── Moderate Risk: 40-70 points
└── High Risk:     > 70 points
```

---

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web interface |
| `/detect` | POST | Single image detection |
| `/batch_detect` | POST | Multiple image detection |
| `/model_info` | GET | Model information |
| `/explainability_info` | GET | Explainability features |

---

## 👨‍💻 Author

**Jagan Developer**
- GitHub: [jagandevloper](https://github.com/jagandevloper)

---

## 📄 License

This project is for educational and research purposes.

