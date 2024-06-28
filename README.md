# Phishing URL Detection Script

This Python script detects potentially phishing URLs using keyword analysis, domain blacklisting, and redirection checks. It utilizes libraries such as `requests`, `urllib.parse`, and `tldextract` for URL parsing and analysis.

## Overview

The script includes two main functions:

### `is_phishing(url)`

Checks if a given URL is suspicious based on:
- **Keyword Analysis:** Looks for suspicious keywords (`secure`, `login`, `account`, etc.) in the URL's path or query parameters.
- **Domain Blacklisting:** Verifies if the domain extracted from the URL is in a predefined list of blacklisted domains.
- **Redirection Analysis:** Checks if the URL redirects to a different domain, a common phishing tactic.

### `is_blacklisted(domain)`

Checks if a provided domain is in a predefined list of blacklisted domains.

## Usage

1. **Clone the repository:**

   bash
   git clone https://github.com/your-username/phishing-url-detection.git
   cd phishing-url-detection
   

2. **Install dependencies (if any):**

   bash
   # Example: pip install requests tldextract
   

3. **Modify the `urls_to_scan` list in the script:**

   Edit the `urls_to_scan` list in `phishing_detection.py` to include the URLs you want to check for phishing indicators.

4. **Run the script:**

   bash
   python phishing_detection.py
   

   The script will output whether each URL in `urls_to_scan` is safe or detected as phishing based on the implemented criteria.

## Example

Here's an example of the `urls_to_scan` list used in the script:

python
urls_to_scan = [
    'http://example.com',
    'https://www.google.com',
    'http://securelogin.com/login.php',
    'https://notphishing.com',
    'http://maliciousdomain.com'
]


## Contact

if you have any queries, feel free to email me at deekshithachavva@gmail.com 

