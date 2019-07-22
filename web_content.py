#!/usr/bin/python

import requests
response =requests('https://so.gushiwen.org/mingju/Default.aspx?p=3')
html = response.read()
print(html)
