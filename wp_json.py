import sys
import requests

def fetch_wp_endpoints(base_url):
    if not base_url.endswith('/'):
        base_url += '/'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                      "AppleWebKit/537.36 (KHTML, like Gecko) " \
                      "Chrome/114.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if 'routes' not in data:
            print("No routes found in the JSON response.")
            return

        for endpoint in data['routes']:
            clean = endpoint.lstrip('/')
            print(clean)

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch: {e}")
    except ValueError:
        print("[ERROR] Invalid JSON received.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wp_json.py <wp-json URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_wp_endpoints(url)
