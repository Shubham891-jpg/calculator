#!/usr/bin/env python3
"""
Quick API Test Script
Run this to verify the server is working correctly
"""

import requests
import json

API_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("Testing /health endpoint...")
    response = requests.get(f"{API_URL}/health")
    if response.status_code == 200:
        print("✅ Health check passed")
        return True
    else:
        print(f"❌ Health check failed: {response.status_code}")
        return False

def test_predict():
    """Test prediction endpoint"""
    print("\nTesting /predict endpoint...")
    
    test_cases = [
        ("All servers are down, complete system failure", "High"),
        ("User needs password reset", "Medium"),
        ("Printer not working in office", "Medium or Low"),
    ]
    
    for ticket_text, expected in test_cases:
        response = requests.post(
            f"{API_URL}/predict",
            json={"ticket_text": ticket_text}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ '{ticket_text[:40]}...'")
            print(f"   Score: {result['severity_score']:.2f} ({result['severity_category']})")
        else:
            print(f"❌ Failed: {response.status_code}")
            return False
    
    return True

def test_batch():
    """Test batch prediction endpoint"""
    print("\nTesting /predict/batch endpoint...")
    
    tickets = [
        "Server is down",
        "Printer not working",
        "Need password reset"
    ]
    
    response = requests.post(
        f"{API_URL}/predict/batch",
        json={"tickets": tickets}
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Batch prediction passed")
        print(f"   Processed {result['total_tickets']} tickets")
        print(f"   Time: {result['processing_time_seconds']:.2f}s")
        return True
    else:
        print(f"❌ Batch prediction failed: {response.status_code}")
        return False

def main():
    print("=" * 60)
    print("IT Ticket Severity Calculator - API Test")
    print("=" * 60)
    
    try:
        # Test all endpoints
        health_ok = test_health()
        if not health_ok:
            print("\n❌ Server is not running or not healthy")
            print("   Start the server with: python ticket/run_server.py")
            return
        
        predict_ok = test_predict()
        batch_ok = test_batch()
        
        print("\n" + "=" * 60)
        if health_ok and predict_ok and batch_ok:
            print("🎉 All tests passed! Server is working perfectly.")
        else:
            print("⚠️  Some tests failed. Check the output above.")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Cannot connect to server")
        print("   Make sure the server is running: python ticket/run_server.py")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
