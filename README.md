# ML Service for Crop Disease Prediction

This is a Flask-based microservice that provides plant disease prediction using deep learning.

## Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### 2. Get a Model

**Option A**: Download pretrained model
```bash
# Place your model file as model.h5
# Model should accept 224x224 RGB images
```

**Option B**: Train your own model
```bash
# Download PlantVillage dataset and extract to dataset/
python train_model.py
```

**Option C**: Run without model (dummy predictions for testing)
```bash
# Service will work but return dummy predictions
python app.py
```

### 3. Start Service

```bash
python app.py
```

Service runs on `http://localhost:5000`

### 4. Test Service

```bash
# Test health
curl http://localhost:5000/health

# Test with existing image
python test_service.py
```

## API Endpoints

### GET /health
Check service status

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### POST /predict
Predict disease from image

**Request:**
- Content-Type: multipart/form-data
- Body: image file (JPEG/PNG)

**Response:**
```json
{
  "success": true,
  "prediction": {
    "disease": "Tomato___Early_blight",
    "plant": "Tomato",
    "condition": "Early_blight",
    "confidence": 0.95,
    "description": "Fungal disease...",
    "remedies": ["Remove infected leaves...", "..."],
    "severity": "moderate"
  },
  "top_predictions": [...]
}
```

## Files

- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `train_model.py` - Model training script
- `download_model.py` - Model download helper
- `test_service.py` - Service testing script
- `model.h5` - Trained model (not in git)

## Supported Diseases (38 classes)

### Plants
- Apple (4 classes)
- Corn/Maize (4 classes)
- Grape (4 classes)
- Tomato (10 classes)
- Potato (3 classes)
- Peach, Pepper, Cherry, Strawberry, etc.

See `app.py` for complete list.

## Model Details

- **Architecture**: MobileNetV2 (transfer learning)
- **Input Size**: 224x224 RGB
- **Output**: 38 classes (softmax)
- **Framework**: TensorFlow/Keras 2.15+

## Development

### Testing
```bash
python test_service.py
```

### Training
```bash
# Requires PlantVillage dataset in dataset/ folder
python train_model.py
```

### Debug Mode
```python
# In app.py
app.run(host='0.0.0.0', port=5000, debug=True)
```

## Production

Use Gunicorn for production:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Or use the PM2 configuration in the parent directory.

## Troubleshooting

### Import Errors
```bash
pip install -r requirements.txt
```

### Model Not Loading
- Check `model.h5` exists and is valid
- Verify TensorFlow version compatibility
- Check file permissions

### Low Memory
- Reduce batch size
- Use smaller model (MobileNetV2 is already small)
- Add more RAM or use cloud GPU

### Slow Predictions
- Use GPU if available
- Reduce image resolution
- Use model quantization

## Resources

- [PlantVillage Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)

# IOT_ML
