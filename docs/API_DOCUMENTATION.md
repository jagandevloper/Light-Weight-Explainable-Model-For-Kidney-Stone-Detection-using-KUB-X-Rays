# 📚 API Documentation

## Kidney Stone Detection System

---

## 🌐 Web API Endpoints

### Base URL
```
http://localhost:5000
```

---

## 📍 Endpoints

### 1. Home Page

**GET** `/`

Returns the web interface for kidney stone detection.

**Response:** HTML page

---

### 2. Detect Kidney Stones

**POST** `/detect`

Analyze an image for kidney stone detection.

**Request:**
- Content-Type: `multipart/form-data`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | File | Yes | Image file (PNG, JPG, JPEG, BMP, TIFF) |
| `confidence` | Float | No | Confidence threshold (0.1-0.9, default: 0.25) |
| `enable_explainability` | Boolean | No | Enable explainability analysis |

**Example Request:**
```javascript
const formData = new FormData();
formData.append('file', imageFile);
formData.append('confidence', 0.25);
formData.append('enable_explainability', true);

fetch('/detect', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

**Success Response (200):**
```json
{
    "success": true,
    "detections": [
        {
            "class": "kidney_stone",
            "confidence": 0.85,
            "bbox": [100, 150, 200, 250],
            "area": 10000
        }
    ],
    "count": 1,
    "inference_time": 15.2,
    "result_image": "base64_encoded_image...",
    "explainability": {
        "gradcam": "base64_encoded_heatmap...",
        "attention_map": "base64_encoded_attention...",
        "clinical_analysis": {
            "risk_level": "Moderate",
            "severity_score": 55,
            "recommendations": ["Consult urologist", "Follow-up scan"]
        }
    }
}
```

**Error Response (400/500):**
```json
{
    "success": false,
    "error": "Error message description"
}
```

---

### 3. Batch Detection

**POST** `/batch_detect`

Process multiple images at once.

**Request:**
- Content-Type: `multipart/form-data`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `files` | Files | Yes | Multiple image files |
| `confidence` | Float | No | Confidence threshold |

**Example Request:**
```javascript
const formData = new FormData();
files.forEach(file => formData.append('files', file));
formData.append('confidence', 0.25);

fetch('/batch_detect', {
    method: 'POST',
    body: formData
})
.then(response => response.json());
```

**Success Response (200):**
```json
{
    "success": true,
    "results": [
        {
            "filename": "image1.jpg",
            "detections": 2,
            "inference_time": 12.5
        },
        {
            "filename": "image2.jpg",
            "detections": 0,
            "inference_time": 11.8
        }
    ],
    "total_images": 2,
    "total_detections": 2,
    "total_time": 24.3
}
```

---

### 4. Model Information

**GET** `/model_info`

Get information about the loaded model.

**Success Response (200):**
```json
{
    "model_loaded": true,
    "model_path": "src/app/models/best.pt",
    "device": "cuda",
    "gpu_name": "NVIDIA GeForce RTX 4050 Laptop GPU",
    "cuda_available": true,
    "model_type": "YOLOv8n",
    "classes": ["kidney_stone"],
    "input_size": 640
}
```

---

### 5. Explainability Information

**GET** `/explainability_info`

Get information about explainability features.

**Success Response (200):**
```json
{
    "available": true,
    "features": {
        "gradcam": true,
        "attention_maps": true,
        "clinical_analysis": true
    },
    "levels": [
        "pixel_level",
        "region_level",
        "image_level"
    ]
}
```

---

## 🔧 Python API

### LightweightKidneyStoneDetector

Main detector class for kidney stone detection.

```python
from src.app.main import LightweightKidneyStoneDetector

# Initialize detector
detector = LightweightKidneyStoneDetector(
    model_path='src/app/models/best.pt',
    device='auto',  # 'auto', 'cuda', or 'cpu'
    enable_half_precision=True
)

# Detect kidney stones
results = detector.detect(
    image_path='path/to/image.jpg',
    confidence_threshold=0.25
)
```

**Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model_path` | str | Required | Path to YOLOv8 model |
| `device` | str | 'auto' | Computing device |
| `enable_half_precision` | bool | True | Use FP16 for faster GPU inference |

**Methods:**

#### `detect(image_path, confidence_threshold=0.25)`
Detect kidney stones in an image.

```python
results = detector.detect('image.jpg', confidence_threshold=0.3)
```

**Returns:**
```python
{
    'detections': [...],
    'count': 1,
    'inference_time': 15.2,
    'annotated_image': numpy_array
}
```

---

### ExplainabilityAnalyzer

Generate visual explanations for detections.

```python
from src.app.utils.explainability import ExplainabilityAnalyzer

analyzer = ExplainabilityAnalyzer(model)

# Generate multi-level explanation
explanation = analyzer.generate_multi_level_explanation(
    image_path='image.jpg',
    detections=results['detections']
)
```

**Methods:**

#### `generate_gradcam(image, detections)`
Generate GradCAM heatmap.

```python
gradcam = analyzer.generate_gradcam(image, detections)
```

#### `generate_attention_map(image, detections)`
Generate attention map visualization.

```python
attention = analyzer.generate_attention_map(image, detections)
```

#### `analyze_clinical_regions(detections, image_shape)`
Perform clinical analysis.

```python
clinical = analyzer.analyze_clinical_regions(detections, image.shape)
```

---

### ClinicalRelevanceAnalyzer

Analyze clinical relevance of detections.

```python
from src.app.utils.clinical_relevance import ClinicalRelevanceAnalyzer

analyzer = ClinicalRelevanceAnalyzer()

# Get clinical prognosis
prognosis = analyzer.analyze(
    detections=results['detections'],
    image_shape=(640, 640)
)
```

**Returns:**
```python
{
    'risk_level': 'Moderate',
    'severity_score': 55,
    'stone_count': 1,
    'total_area': 1500,
    'recommendations': [
        'Consult urologist',
        'Increase water intake',
        'Follow-up scan in 3 months'
    ],
    'anatomical_location': 'Right kidney - lower pole'
}
```

---

## 📊 Response Codes

| Code | Status | Description |
|------|--------|-------------|
| 200 | OK | Request successful |
| 400 | Bad Request | Invalid parameters or file |
| 413 | Payload Too Large | File exceeds 16MB limit |
| 500 | Server Error | Internal server error |

---

## 📁 Supported File Formats

| Format | Extension | Max Size |
|--------|-----------|----------|
| PNG | .png | 16 MB |
| JPEG | .jpg, .jpeg | 16 MB |
| BMP | .bmp | 16 MB |
| TIFF | .tiff, .tif | 16 MB |
| GIF | .gif | 16 MB |

---

## 🔗 Example Usage

### JavaScript (Frontend)
```javascript
async function detectKidneyStones(imageFile) {
    const formData = new FormData();
    formData.append('file', imageFile);
    formData.append('confidence', 0.25);
    formData.append('enable_explainability', true);

    const response = await fetch('/detect', {
        method: 'POST',
        body: formData
    });

    return await response.json();
}
```

### Python (Requests)
```python
import requests

# Single image detection
with open('kidney_image.jpg', 'rb') as f:
    response = requests.post(
        'http://localhost:5000/detect',
        files={'file': f},
        data={'confidence': 0.25}
    )
    result = response.json()
    print(f"Detections: {result['count']}")
```

### cURL
```bash
# Detect kidney stones
curl -X POST http://localhost:5000/detect \
  -F "file=@kidney_image.jpg" \
  -F "confidence=0.25"

# Get model info
curl http://localhost:5000/model_info
```

---

## 📞 Support

For API issues or questions:
- Open an issue on [GitHub](https://github.com/jagandevloper/Light-Weight-Explainable-Model-For-Kidney-Stone-Detection-using-KUB-X-Rays)
- Check the [Installation Guide](INSTALLATION.md)
