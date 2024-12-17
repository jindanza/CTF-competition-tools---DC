import requests

directories = [
    "admin", "hidden", "private", "config", "data", "backup", "ctf", 
    "flag", "secret", "secure", "test", "dev"
]

base_url = "https://website2.mbclaboratory.com/"

for directory in directories:
    url = f"{base_url}{directory}/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Found: {url}")
            print(f"Content: {response.text}")
        elif response.status_code == 403:
            print(f"Forbidden: {url} (access restricted)")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
