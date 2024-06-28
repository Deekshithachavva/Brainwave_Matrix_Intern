# Phishing URL Detection Script

This Python script detects potentially phishing URLs using keyword analysis, domain blacklisting, and redirection checks. It utilizes libraries such as requests, urllib.parse, and tldextract for URL parsing and analysis.

## Overview

The script includes two main functions:

### is_phishing(url)

Checks if a given URL is suspicious based on:
- *Keyword Analysis:* Looks for suspicious keywords (secure, login, account, etc.) in the URL's path or query parameters.
- *Domain Blacklisting:* Verifies if the domain extracted from the URL is in a predefined list of blacklisted domains.
- *Redirection Analysis:* Checks if the URL redirects to a different domain, a common phishing tactic.

### is_blacklisted(domain)

Checks if a provided domain is in a predefined list of blacklisted domains.

## Usage

1. *Clone the repository:*

   ```bash
   git clone https://github.com/your-username/phishing-url-detection.git
   cd phishing-url-detection

2. install dependencies (if any):
 
   ```bash
   # Example: pip install requests tldextract

3. *modify the 'urls_to_scan' list in the script:* edit the 'urls_to_scan' list in 'phishing_detection.py' to include the URLs we want to check for phishing indicators.
4. *run the script :*
   ```bash
   python phishing_detection.py
 the script will output whether each URL in 'urls_to_scan' is safe or not as phishing based on the implemented criteria.
 
7. 
8. 
9. 
