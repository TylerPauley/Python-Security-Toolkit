import whois, dns.resolver, re, socket, requests, ssl

def banner_grab(domain, port=80):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        
        if port == 443: # Makes SSL to try HTTPS
            context = ssl.create_default_context()
            sock = context.wrap_socket(sock, server_hostname=domain)
        
        sock.connect((domain, port))
        request = f"GET / HTTP/1.1\r\nHost: {domain}\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0\r\nConnection: close\r\n\r\n"
        sock.send(request.encode())
        banner = sock.recv(1024).decode()
        print(f"Banner (Port {port}):\n{banner}")
        sock.close()
    except Exception as e:
        print(f"Could not retrieve banner on port {port}: {e}")

def hostname(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Domain IP address: {ip_address}")
    except socket.gaierror as e:
        print(f"Could not resolve IP address: {e}")

def whois_lookup(domain):
    try:
        return whois.whois(domain)
    except Exception as e:
        print(f"Error during WHOIS lookup: {e}")

def check_website_status(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
    }
    for protocol in ['http', 'https']:
        full_url = f"{protocol}://{url}"
        try:
            response = requests.get(full_url, headers=headers)
            print(f"Website Status ({protocol}): {response.status_code}")
        except requests.ConnectionError:
            print(f"Failed to connect to {full_url}")

def mx_records(domain):
    try:
        dns_results = dns.resolver.resolve(domain, 'MX')
        for resolver_data in dns_results:
            print(f"Host: {resolver_data.exchange} has preference: {resolver_data.preference}")
    except Exception as e:
        print(f"Could not retrieve MX records: {e}")

def run_all(domain):
    print(f"Running all checks for {domain}...\n")
    hostname(domain)
    mx_records(domain)
    whois_info = whois_lookup(domain)
    if whois_info:
        print(f"WHOIS Lookup:\n{whois_info}")
    check_website_status(domain)
    banner_grab(domain, 80)   # Try banner grab on HTTP port 80
    banner_grab(domain, 443)  # Try banner grab on HTTPS port 443

def main():
    domain_input = input("Enter the domain you'd like to analyze >> ")

    # Extract domain from the URL if it includes 'http' or 'https'
    pattern = r'https?://([^/]+)'  # Handles both http and https
    domain_match = re.search(pattern, domain_input)
    domain = domain_match.group(1) if domain_match else domain_input

    print("\nChoose an option:")
    print("1. IP Resolution")
    print("2. MX Records")
    print("3. WHOIS Lookup")
    print("4. Website Status Check")
    print("5. Banner Grabbing")
    print("6. All of the above")
    choice = input("\nWhich option do you choose? >> ")

    if choice == "1":
        hostname(domain)
    elif choice == "2":
        mx_records(domain)
    elif choice == "3":
        whois_info = whois_lookup(domain)
        if whois_info:
            print(f"WHOIS Lookup:\n{whois_info}")
    elif choice == "4":
        check_website_status(domain)
    elif choice == "5":
        banner_grab(domain, 80)
        banner_grab(domain, 443)  # Try both ports 80 (HTTP) and 443 (HTTPS)
    elif choice == "6":
        run_all(domain)
    else:
        print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
