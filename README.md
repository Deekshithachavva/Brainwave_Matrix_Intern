#TASK1- Phishing URL Detection Script

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
   git clone https://github.com/Deekshithachavva/Brainwave_Matrix_Intern/edit/main/scan_phishing.py
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








# Task 2: Password Validation Tool

This project is a password validation tool implemented in Python using Jupyter Notebook with ipywidgets. The tool helps users assess the strength of their passwords based on specified security criteria.

## Overview

In today's digital age, strong password practices are essential for protecting personal and sensitive information. This tool provides an interactive way to check if a password meets commonly accepted security standards.

## Features

The password validation tool checks for the following criteria:

1. *Minimum Length*: The password must be at least 8 characters long.
2. *Uppercase Letter*: The password must contain at least one uppercase letter (A-Z).
3. *Lowercase Letter*: The password must contain at least one lowercase letter (a-z).
4. *Digit*: The password must include at least one numerical digit (0-9).
5. *Special Character*: The password must contain at least one special character, such as !@#$%^&*(),.?":{}|<>.

## Requirements

To run this project, you will need:
- Python 3.x
- Jupyter Notebook or Google Colab
- ipywidgets library for interactive widgets

## Installation Instructions

1. *Set Up Environment*:
   - If using Jupyter Notebook, ensure you have Python 3 installed.
   - If using Google Colab, no installation is needed as it runs in the cloud.

2. *Install ipywidgets*:
   - If using Jupyter Notebook, run the following command in a cell:
     bash
     pip install ipywidgets
     
   - In Google Colab, run the following command:
     bash
     !pip install ipywidgets
     

## How to Use

1. Open the Jupyter Notebook or Google Colab notebook containing the password validation code.
2. Execute the cell to display the password input widget.
3. Enter your desired password in the input field.
4. Click the "Check Password" button to validate the password.
5. The result will be shown below the button, indicating whether the password is valid or not based on the specified criteria.

## Example Scenarios

- *Valid Password*: 
  - P@ssw0rd123 (meets all criteria)
  
- *Invalid Password*: 
  - password (missing uppercase, digit, and special character)
  - Password123 (missing special character)
  - 12345678 (missing uppercase and lowercase letters)


## Contact

if you have any queries, feel free to email me at deekshithachavva@gmail.com 

