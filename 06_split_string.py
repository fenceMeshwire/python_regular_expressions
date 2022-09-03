#!/usr/bin/env python3

# Python 3.9.5

# 06_split_string.py

# Dependency
import re

str_text = 'Statements in JavaScript are closed with a semicolon; List elements in Python are separated with a, if conditions end with:'

# Split the string by using the regex below:
result = re.split(r'(?:,|;|:|\s)\s*', str_text)

# Append only the words len(word) > 0:
result = [word for word in result if not word == '']

print(result)
