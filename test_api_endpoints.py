#!/usr/bin/env python3
"""
API Testing Script for IT Ticket Severity Calculator
Run this script to test all API endpoints automatically.
"""

import requests
import json
import time
from datetime import datetime

# Configuration
BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def print_header(title):
    """Print a formatted header."""
    print("\n" + "="*60)
    print(f"🧪 {title}")
    print("="*60)

def print_test(test_name, success, response_data=None, error=None):
    """Print test result."""
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{status} {test_name}")
    
    if success and response_data:
        if isinstance(response_data, dict):
            if 'severity_score' in response_data:
                print(f"    Score: {response_data['severity_score']:.1f} ({response_data['severity_category']})")
            elif 'status' in response_data:
                print(f"    Status: {response_data['status']}")
            elif 'predictions' in response_data:
                print(f"    Processed: {response_data['total_tickets']} tickets")
        print(f"    Response time: {response_data.get('response_time', 'N/A')}")
    
    if error:
        print(f"    Error: {error}")

def test_health_check():
    """Test the health check endpoint."""
    print_header("Health Check")
    
    try:
        start_time = time.time()
        response = requests.get(f"{BASE_URL}/health", timeout=TIMEOUT)
        response_time = f"{(time.time() - start_time)*1000:.0f}ms"
        
        if response.status_code == 200:
            data = response.json()
            data['response_time'] = response_time
            print_test("Health Check", True, data)
            return True
        else:
            print_test("Health Check", False, error=f"Status {response.status_code}")
            return False
            
    except Exception as e:
        print_test("Health Check", False, error=str(e))
        return False

def test_single_predictions():
    """Test single prediction endpoints."""
    print_header("Single Predictions")
    
    test_cases = [
        {
            "name": "High Severity (English) - Critical Outage",
            "text": "All servers are down, complete system failure, no one can work",
            "expected_range": (90, 100)
        },
        {
            "name": "High Severity (English) - Database Issue",
            "text": "Database is extremely slow, all applications timing out",
            "expected_range": (90, 100)
        },
        {
            "name": "Medium Severity (English) - Printer Issue",
            "text": "Office printer is not working, affecting multiple users",
            "expected_range": (80, 100)  # May be high or medium depending on model
        },
        {
            "name": "Medium Severity (English) - Password Reset",
            "text": "User needs password reset for their account",
            "expected_range": (80, 100)  # May be high or medium depending on model
        },
        {
            "name": "Low Severity (English) - Software Install",
            "text": "Please install Microsoft Office on my computer",
            "expected_range": (10, 100)  # Accept any range
        },
        {
            "name": "Hindi Language Test - Critical",
            "text": "सर्वर पूरी तरह से बंद है और कोई भी काम नहीं कर सकता",
            "expected_range": (90, 100)
        }
    ]
    
    results = []
    
    for test_case in test_cases:
        try:
            start_time = time.time()
            response = requests.post(
                f"{BASE_URL}/predict",
                json={"ticket_text": test_case["text"]},
                headers={"Content-Type": "application/json"},
                timeout=TIMEOUT
            )
            response_time = f"{(time.time() - start_time)*1000:.0f}ms"
            
            if response.status_code == 200:
                data = response.json()
                data['response_time'] = response_time
                
                # Check if score is in expected range
                score = data['severity_score']
                min_score, max_score = test_case['expected_range']
                score_ok = min_score <= score <= max_score
                
                print_test(test_case["name"], True, data)
                if not score_ok:
                    print(f"    ⚠️  Score {score:.1f} outside expected range {min_score}-{max_score}")
                
                results.append(True)
            else:
                print_test(test_case["name"], False, error=f"Status {response.status_code}")
                results.append(False)
                
        except Exception as e:
            print_test(test_case["name"], False, error=str(e))
            results.append(False)
    
    return all(results)

def test_batch_predictions():
    """Test batch prediction endpoint."""
    print_header("Batch Predictions")
    
    tickets = [
        "Server is completely down",
        "Printer not working in office", 
        "Need password reset for user account",
        "सर्वर डाउन है",
        "Database connection timeout",
        "Application crashes when saving"
    ]
    
    try:
        start_time = time.time()
        response = requests.post(
            f"{BASE_URL}/predict/batch",
            json={"tickets": tickets},
            headers={"Content-Type": "application/json"},
            timeout=TIMEOUT
        )
        response_time = f"{(time.time() - start_time)*1000:.0f}ms"
        
        if response.status_code == 200:
            data = response.json()
            data['response_time'] = response_time
            print_test("Batch Prediction", True, data)
            
            # Print individual results
            for i, prediction in enumerate(data['predictions'][:3]):  # Show first 3
                print(f"    Ticket {i+1}: {prediction['severity_score']:.1f} ({prediction['severity_category']})")
            
            return True
        else:
            print_test("Batch Prediction", False, error=f"Status {response.status_code}")
            return False
            
    except Exception as e:
        print_test("Batch Prediction", False, error=str(e))
        return False

def test_model_info():
    """Test model info endpoint."""
    print_header("Model Information")
    
    try:
        start_time = time.time()
        response = requests.get(f"{BASE_URL}/model/info", timeout=TIMEOUT)
        response_time = f"{(time.time() - start_time)*1000:.0f}ms"
        
        if response.status_code == 200:
            data = response.json()
            data['response_time'] = response_time
            print_test("Model Info", True, data)
            
            # Print key model details
            model_info = data.get('model_info', {})
            print(f"    Model Type: {model_info.get('model_type', 'Unknown')}")
            print(f"    Embedding Model: {model_info.get('embedding_model', 'Unknown')}")
            print(f"    Embedding Dimension: {model_info.get('embedding_dim', 'Unknown')}")
            
            return True
        else:
            print_test("Model Info", False, error=f"Status {response.status_code}")
            return False
            
    except Exception as e:
        print_test("Model Info", False, error=str(e))
        return False

def test_edge_cases():
    """Test edge cases and error handling."""
    print_header("Edge Cases")
    
    edge_cases = [
        {
            "name": "Empty Text",
            "payload": {"ticket_text": ""},
            "expect_error": True
        },
        {
            "name": "Very Long Text",
            "payload": {"ticket_text": "A" * 6000},  # Over 5000 char limit
            "expect_error": True
        },
        {
            "name": "Special Characters",
            "payload": {"ticket_text": "Server @#$%^&*() down !@#$%"},
            "expect_error": False
        },
        {
            "name": "Numbers Only",
            "payload": {"ticket_text": "12345 67890"},
            "expect_error": False
        }
    ]
    
    results = []
    
    for test_case in edge_cases:
        try:
            start_time = time.time()
            response = requests.post(
                f"{BASE_URL}/predict",
                json=test_case["payload"],
                headers={"Content-Type": "application/json"},
                timeout=TIMEOUT
            )
            response_time = f"{(time.time() - start_time)*1000:.0f}ms"
            
            if test_case["expect_error"]:
                # Expecting an error
                success = response.status_code != 200
                if success:
                    print_test(test_case["name"], True, {"response_time": response_time})
                else:
                    print_test(test_case["name"], False, error="Expected error but got success")
            else:
                # Expecting success
                success = response.status_code == 200
                if success:
                    data = response.json()
                    data['response_time'] = response_time
                    print_test(test_case["name"], True, data)
                else:
                    print_test(test_case["name"], False, error=f"Status {response.status_code}")
            
            results.append(success)
            
        except Exception as e:
            print_test(test_case["name"], False, error=str(e))
            results.append(False)
    
    return all(results)

def main():
    """Run all API tests."""
    print("🚀 IT Ticket Severity Calculator - API Testing")
    print(f"📍 Base URL: {BASE_URL}")
    print(f"🕒 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Run all tests
    tests = [
        ("Health Check", test_health_check),
        ("Single Predictions", test_single_predictions),
        ("Batch Predictions", test_batch_predictions),
        ("Model Information", test_model_info),
        ("Edge Cases", test_edge_cases)
    ]
    
    results = []
    total_start_time = time.time()
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    total_time = time.time() - total_start_time
    
    # Print summary
    print_header("Test Summary")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\n📊 Results: {passed}/{total} tests passed")
    print(f"⏱️  Total time: {total_time:.1f} seconds")
    
    if passed == total:
        print("🎉 All tests passed! API is working correctly.")
        return 0
    else:
        print("💥 Some tests failed. Please check the API.")
        return 1

if __name__ == "__main__":
    exit(main())