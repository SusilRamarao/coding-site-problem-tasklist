from bs4 import BeautifulSoup

import requests


URL = "https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/"
r = requests.get(URL)
#print(r.content)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())

"""

TODOs:
1) Write script to fetch the leetcode and geeks for geeks related problem urls from the website.
2) Use the leetcode-api to get the solved and unsolved problems 
3) Construct a minimalistic website to show what are solved and unsolved in local.
4) Use a easy database functionality to store already entered problems.

Website
It should have two tabs one for showing already entered problems
and another tab to enter the new URL and add the problems from that website.
"""


