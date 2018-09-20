## cred-harvester-stuffer

Given a phishing website and the correct headers from a test HTTP POST request
Set the user-agent to a version of Chrome, a referer of Google, and send 4k usernames/passwords to the site

Usernames are imported from random_names.py as a list containing a set of first, last name combined
and appended with a random number between 1 and 12 then have a random free email domain appended.

Passwords are randomly generated alphanumeric and special characters between 12 and 25 chars long

## Prerequisites
`pip install requests`
