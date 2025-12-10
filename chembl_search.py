import requests
import json
import csv

BASE_URL = "https://www.ebi.ac.uk/chembl/api/data"

def test_api_connection():
    """Test if ChEMBL API is accessible"""
    try:
        response = requests.get(f"{BASE_URL}/status", timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"Connection error: {e}")
        return False

# Test: Verify imports work without errors
print("Imports successful")
print(f"requests version: {requests.__version__}")

# Test: Check API connectivity
if test_api_connection():
    print("✓ API connection successful")
else:
    print("✗ API connection failed")

