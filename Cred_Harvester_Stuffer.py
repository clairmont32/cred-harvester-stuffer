"""
Given a phishing website and the correct headers from a test HTTP POST request
Set the user-agent to a version of Chrome, a referer of Google, and send 4k usernames/passwords to the site

Usernames are imported from random_names.py as a list containing a set of first, last name combined
and appended with a random number between 1, 12 then have a random free email domain appended.

Passwords are randomly generated alphanumeric and special characters between 12 and 25 chars long
"""

import string
import random
import requests
import random_names

requests.urllib3.disable_warnings()

# ask user for appropriate site info
url = str(input('Enter URL: '))
username_header = str(input('Enter the username header: '))
password_header = str(input('Enter the password header: '))

# set User-Agent to Chrome to slightly masquerade that we're automating these requests 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36', 'Referer': 'https://google.com'}

# merge a set of first/last names (sets within a list) together into a new list
usernames = [''.join(name).lower() for name in random_names.names]

# list of domains to allow for a bit of randomness to the stuffed emails
domains = ['@gmail.com', '@yahoo.com', '@outlook.com', '@ymail.com', '@mail.ru', '@mail.me']

# iterate through the list of usernames and give some randomness to the credentials and domains
for username in usernames:
    username = username + str(random.randint(1, 12)) + random.choice(domains)
    # create a pseudo-random alphanumeric string with special chars between 12 and 25 chars long
    password = ''.join(
        [random.choice(string.ascii_letters + string.digits + '!@#$*()-+') for x in range(random.randint(12, 25))])
    try:
        r = requests.post(url, allow_redirects=False, headers=headers, verify=False, data={username_header: username, password_header: password})
        if r.status_code is not 200:
            # just in case something is allowed but doesnt accept the stuffed cred
            raise requests.RequestException
        else:
            print('Sending {!s} with a password of {!s}'.format(username, password))
    except requests.RequestException as error:
        print('Received HTTP ' + str(r.status_code))
        print(error)
        exit(1)
