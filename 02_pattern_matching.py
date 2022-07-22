#!/usr/bin/env python3

# Python 3.9.5

# 02_pattern_matching.py

# Dependency
import re

sample_text:str = """A quiet summer morning had risen up upon the great city. The clock in
the modern church steeple of the downtown district had not yet struck
seven, when the side door of one of the small buildings closed and a woman
came out into the silent street."""

# . matches any character for each dot
search_string = 's....r'
findings = re.findall(search_string, sample_text)
print(findings) # returns ['summer']

# \w matches alphanumeric characters: [0-9a-zA-Z_] for each \w
search_string = 's\w\w\w\wr'
findings = re.findall(search_string, sample_text)
print(findings) # returns ['summer']

# .*? matches any character until the escape character '?' for non-greedy matching
search_string = 'b.*?s'
findings = re.findall(search_string, sample_text)
print(findings) # returns ['buildings']
