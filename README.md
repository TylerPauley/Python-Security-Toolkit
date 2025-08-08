
# Cybersecurity Python Scripts

This repository contains various Python scripts that demonstrate basic automation and utilize APIs for cybersecurity-related tasks. Below is a description of each script along with instructions on how to run them.

## Scripts Included

1. **DomainProbe.py**
2. **File_hash.py**
3. **Password_Strength_Checker.py**
4. **VT_URL_Checker.py** (VirusTotal URL Reputation Checker)
5. **PortGuesser.py**

---

### 1. DomainProbe.py

**Description:**
This script provides multiple functionalities for analyzing websites, such as:
- Retrieving the website's IP address.
- Performing an MX (Mail Exchange) DNS lookup.
- Conducting a WHOIS lookup for domain registration information.
- Checking the website's status (HTTP/HTTPS).
- Performing banner grabbing from open ports (80 and 443).

**Usage:**
```bash
python DomainProbe.py
```
Follow the prompts to enter a domain, and select the desired operation or choose to run all checks at once.

**Requirements:**
- `whois`, `requests`, `dns.resolver`, and `socket` libraries.

---

### 2. File_hash.py

**Description:**
This script generates MD5, SHA1, and SHA256 checksums for files. It's useful for verifying file integrity and checking for file tampering.

**Usage:**
```bash
python File_hash.py
```
You will be prompted to enter the file name. Make sure the file is in the same directory as the script, or provide the correct file path.

**Requirements:**
- `hashlib`, `os` libraries.

---

### 3. Password_Strength_Checker.py

**Description:**
This script checks the strength of a password based on common patterns and conditions like:
- Minimum length.
- Presence of lowercase, uppercase letters, numbers, and special characters.
- Identifies weak patterns such as consecutive characters or repeated sequences.

**Usage:**
```bash
python Password_Strength_Checker.py
```
Input a password, and the script will return a strength analysis based on the criteria mentioned.

**Requirements:**
- None (uses basic Python functions).

---

### 4. VT_URL_Checker.py

**Description:**
This script uses the VirusTotal API to check the reputation of a URL. It sends the URL to VirusTotal and retrieves how many antivirus engines have flagged the URL as malicious.

**Usage:**
1. Add your VirusTotal API key in a separate file `API_Keys.py` in the format:
   ```python
   VT_API_KEY = 'your_virustotal_api_key'
   ```
2. Run the script:
   ```bash
   python VT_URL_Checker.py
   ```
3. Input the URL you'd like to check.

**Requirements:**
- `requests` library.
- VirusTotal API key (Free API keys allow limited requests per minute).

---

## Installation

To use these scripts, make sure you have Python installed. You can install the necessary libraries using `pip`:

```bash
pip install requests python-whois dnspython
```

Clone the repository:

```bash
git clone https://github.com/TylerPauley/pythonScripts.git
```

Navigate to the repository directory and run any of the scripts using Python.

---

## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvement.

---

## License

This repository is licensed under the MIT License.
