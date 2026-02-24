import requests
from datetime import datetime

def check_google():
    try:
        response = requests.get('https://www.google.com', timeout=5)
        timestamp = datetime.now().isoformat()
        status_code = response.status_code
        
        print(f"Hello World!")
        print(f"Timestamp: {timestamp}")
        print(f"HTTP Status: {status_code}")
        
        return {
            "timestamp": timestamp,
            "status": status_code,
            "success": True
        }
    except requests.exceptions.RequestException as e:
        timestamp = datetime.now().isoformat()
        print(f"Hello World!")
        print(f"Timestamp: {timestamp}")
        print(f"Error checking Google: {e}")
        
        return {
            "timestamp": timestamp,
            "status": None,
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    check_google()