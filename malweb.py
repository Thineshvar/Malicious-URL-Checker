import requests
import json

def check_website_safety(api_key, website):
    url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"

    payload = {
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],  # Use valid threat types
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": website}]
        }
    }
    
    response = requests.post(url, json=payload)

    # Print status code and response text for debugging
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.ok:
        data = response.json()

        if 'matches' in data:
            print(f"The website {website} is malicious!")
        else:
            print(f"The website {website} is safe!")
    else:
        print('Something went wrong, please try again!')

if __name__ == "__main__":
    api_key = "AIzaSyCMR1KjGHSygGKDxSxL_hkoaQkMrLbgzuw"  # Replace with your actual API key
    website = input('Enter website URL: ')
    check_website_safety(api_key, website)
