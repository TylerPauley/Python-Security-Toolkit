import requests, time
from API_Keys import VT_API_KEY

# I have the API key in a seperate .py file as I find it easier and more secure than putting it into the script. 
# Below I added the VT_API_KEY format if you'd like to add your own API key to test the script. 

# VT_API_KEY = 'VirusTotal API Key'

def check_url_reputation(url):
    base_url = "https://www.virustotal.com/vtapi/v2/url/report"
    
    # Set parameters for the API request
    params = {'apikey': VT_API_KEY, 'resource': url}
    
    response = requests.get(base_url, params=params)
    
    # Check to see if the request was successful
    if response.status_code == 200:
        result = response.json()
        
        ##print(f"\n\n{result}\n\n")

        # Extract and print relevant data from the response
        if result['response_code'] == 1:
            positives = result['positives']
            total = result['total']
            print(f"URL: {url}")
            print(f"Positives: {positives}/{total} engines flagged this URL as malicious.")
            
            # Could make this part more complex, but the script already shows how many vendors found the URL
            # as malicious. There's always a chance for a false positive, so that's why I added the 2 or more.
            if positives >= 2:
                print("This URL has been flagged by 2 or more security vendor's as potentially dangerous!")
            else:
                print("This URL appears to be clean.")
        else:
            print("No data found for this URL.")
    else:
        print(f"Error: Unable to retrieve data. Status code: {response.status_code}")

def is_valid_url(url):
    # Check if the input has at least one period and characters on both sides of the period
    if '.' in url and not url.startswith('.') and not url.endswith('.'):
        return True
    print(f"Invalid domain name: {url}\nIt looks like the domain is incomplete. Please ensure you include a valid top-level domain (e.g., .com, .org, .net) at the end.")
    return False

if __name__ == "__main__":
    url_to_check = input("Enter a URL to check its reputation: ")
    
    if is_valid_url(url_to_check):
        if not url_to_check.startswith(('http://', 'https://')):
            url_to_check = 'http://' + url_to_check

        # Adding a delay as the API only have 4 requests per minute on the free plan.
        time.sleep(15) 
        check_url_reputation(url_to_check)
