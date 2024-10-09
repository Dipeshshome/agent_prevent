import requests
from config import API_CONFIG, get_api_headers

def fetch_conversations(resident_id,resident_name, event_type):
    url = f"{API_CONFIG['base_url']}/conversations/?resident_id={resident_id}&resident_name={resident_name}&event_type={event_type}"
    print(url)
    headers = get_api_headers()

    print(f"Fetching data from: {url}")

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching conversations: {response.status_code}")

