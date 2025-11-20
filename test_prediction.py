#!/usr/bin/env python3
"""
Test script for BD Crop Disease Detection API
Tests the prediction endpoint with a sample image
"""

import requests
import json
import os
from pathlib import Path

# Configuration
API_URL = "http://192.168.0.115:5000"  # Change if your API is running on a different host/port
IMAGE_PATH = "images/istockphoto-1199805689-170667a.jpg"

def test_health_check():
    """Test the health check endpoint"""
    print("=" * 70)
    print("🏥 Testing Health Check Endpoint")
    print("=" * 70)
    
    try:
        response = requests.get(f"{API_URL}/health", timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"✅ Health Check: {json.dumps(data, indent=2)}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Health Check Failed: {e}")
        return False

def test_prediction(image_path):
    """Test the prediction endpoint with an image"""
    print("\n" + "=" * 70)
    print("🔍 Testing Prediction Endpoint")
    print("=" * 70)
    
    # Check if image exists
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        print(f"   Current directory: {os.getcwd()}")
        return None
    
    print(f"📸 Loading image: {image_path}")
    file_size = os.path.getsize(image_path)
    print(f"   File size: {file_size / 1024:.2f} KB")
    
    try:
        # Prepare the image file
        with open(image_path, 'rb') as img_file:
            files = {'image': (os.path.basename(image_path), img_file, 'image/jpeg')}
            
            print(f"\n📤 Sending prediction request to {API_URL}/predict...")
            response = requests.post(
                f"{API_URL}/predict",
                files=files,
                timeout=60  # Longer timeout for model loading
            )
            
            response.raise_for_status()
            result = response.json()
            
            # Display results
            print("\n" + "=" * 70)
            print("📊 PREDICTION RESULTS")
            print("=" * 70)
            
            if result.get('success'):
                prediction = result.get('prediction', {})
                disease = prediction.get('disease', 'Unknown')
                confidence = prediction.get('confidence', 0)
                model_used = prediction.get('model_used', 'Unknown')
                guidance = prediction.get('guidance', {})
                low_confidence = prediction.get('low_confidence', False)
                
                print(f"\n🌾 Disease Detected: {disease}")
                print(f"📈 Confidence: {confidence * 100:.2f}%")
                if low_confidence:
                    print(f"⚠️  WARNING: Low confidence prediction")
                print(f"🤖 Model Used: {model_used}")
                
                # Show warning if present
                warning = result.get('warning')
                if warning:
                    print(f"\n⚠️  {warning}")
                suggestion = result.get('suggestion')
                if suggestion:
                    print(f"💡 Suggestion: {suggestion}")
                
                # Display guidance
                if guidance:
                    print(f"\n📋 Guidance:")
                    print(f"   Description: {guidance.get('description', 'N/A')}")
                    print(f"   Severity: {guidance.get('severity', 'N/A')}")
                    
                    remedies = guidance.get('remedies', [])
                    if remedies:
                        print(f"   Remedies:")
                        for i, remedy in enumerate(remedies, 1):
                            print(f"      {i}. {remedy}")
                    
                    follow_up = guidance.get('follow_up')
                    if follow_up:
                        print(f"   Follow-up: {follow_up}")
                    
                    source = guidance.get('source', 'N/A')
                    print(f"   Source: {source}")
                
                # Determine if healthy or diseased
                disease_lower = disease.lower()
                if "healthy" in disease_lower:
                    print(f"\n✅ Plant appears HEALTHY")
                else:
                    print(f"\n⚠️  Plant may have DISEASE: {disease}")
                
                return result
            else:
                error = result.get('error', 'Unknown error')
                print(f"\n❌ Prediction Failed: {error}")
                suggestion = result.get('suggestion')
                if suggestion:
                    print(f"💡 Suggestion: {suggestion}")
                # Still return result if it has prediction data (for debugging)
                raw_prediction = result.get('raw_prediction')
                if raw_prediction:
                    print(f"📊 Raw Prediction: {raw_prediction}")
                    print(f"📈 Confidence: {result.get('confidence', 0) * 100:.2f}%")
                return None
                
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The model may still be loading.")
        print("   Please wait a few seconds and try again.")
        return None
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection failed. Is the API running at {API_URL}?")
        print("   Start the API with: python app.py")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """Main test function"""
    print("\n" + "🌾" * 35)
    print("BD Crop Disease Detection API - Test Script")
    print("🌾" * 35 + "\n")
    
    # Test health check first
    if not test_health_check():
        print("\n⚠️  Health check failed. Make sure the API is running.")
        print("   Start the API with: python app.py")
        return
    
    # Test prediction
    result = test_prediction(IMAGE_PATH)
    
    if result:
        print("\n" + "=" * 70)
        print("✅ Test completed successfully!")
        print("=" * 70)
    else:
        print("\n" + "=" * 70)
        print("❌ Test failed. Check the errors above.")
        print("=" * 70)

if __name__ == "__main__":
    main()

