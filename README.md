# Python Security Toolkit

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.9+-brightgreen.svg)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

A versatile collection of Python scripts designed for security analysis, reconnaissance, and educational purposes. This toolkit is built to be simple, effective, and easily extensible.

---

## 🚀 About The Project

This repository was created to bring together a variety of useful scripts for cybersecurity enthusiasts, students, and professionals. Whether you're analyzing a domain, checking file integrity, or practicing your knowledge of network protocols, these tools are designed to help. The focus is on clean, readable code that can be used for practical tasks and serve as a learning resource.

---

## ✨ Features

-   **Domain Analysis**: Perform DNS, WHOIS, and MX lookups.
-   **Threat Intelligence**: Check URL reputations against the VirusTotal API.
-   **File Integrity**: Calculate MD5, SHA1, and SHA256 checksums for any file.
-   **Password Security**: Analyze password strength against common criteria.
-   **Educational Tools**: Includes a gamified quiz to help memorize common network ports.

---

## 🧰 The Toolkit

| Script                  | Description                                                                  | Key Libraries        |
| :---------------------- | :--------------------------------------------------------------------------- | :------------------- |
| `domain_analyzer.py`      | Gathers intelligence on a domain, including IP, WHOIS, and MX records.       | `whois`, `dns.resolver` |
| `virustotal_checker.py` | Checks a URL's reputation using the VirusTotal API.                        | `requests`           |
| `file_checksum.py`      | Generates MD5, SHA1, and SHA256 hashes to verify file integrity.             | `hashlib`            |
| `password_strength.py`  | Evaluates a password's strength based on length, complexity, and patterns.   | (standard libraries) |
| `port_quiz.py`          | An interactive command-line game to help memorize network ports and services. | `random`             |

---

## ⚙️ Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.9 or later
-   `pip` package manager

### Installation

1.  **Clone the repository:**

    ```
    git clone [https://github.com/TylerPauley/Python-Security-Toolkit.git](https://github.com/TylerPauley/Python-Security-Toolkit.git)
    cd Python-Security-Toolkit
    ```

2.  **Install the required libraries:**
    It is recommended to use a virtual environment.

    ```
    pip install -r requirements.txt
    ```

3.  **Set up your API Key (for `virustotal_checker.py`):**
    -   Create a file named `api_keys.py`.
    -   Inside the file, add your VirusTotal API key like this:

        ```
        VT_API_KEY = 'your_virustotal_api_key_here'
        ```

---

## ▶️ Usage

Navigate to the repository directory and run any script using Python.

**Example: Running the Domain Analyzer**
python domain_analyzer.py

The script will then prompt you for the necessary inputs.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact

Tyler Pauley - [LinkedIn](https://linkedin.com/in/tylerpauleysecurity) - [GitHub Profile](https://github.com/TylerPauley)
