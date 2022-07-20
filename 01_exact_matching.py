#!/usr/bin/env python3

# Python 3.9.5

# 01_exact_matching.py

# Dependency
import re

sample_text:str = """A quiet summer morning had risen up upon the great city. The clock in
the modern church steeple of the downtown district had not yet struck
seven, when the side door of one of the small buildings closed and a woman
came out into the silent street."""

# EXACT MATCHING:
result:list = re.findall("silent", sample_text)
print(result)

# Access the word in the given string:
start:int = re.search("silent", sample_text).start()
end:int = re.search("silent", sample_text).end()

word:str = sample_text[start:end] 
print(word)

# COMBINE THE KEYWORD WITH ADDITIONAL CHARACTERS INTO A SEARCH PHRASE:
sample_text:str = """The spreadsheet contains information about the Vehicle Identification Number (VIN)."""

keyword:str = 'VIN'
search_phrase:str = r'\s' + '\(' + keyword + '\)'

finding:list = re.findall(search_phrase, sample_text)
print(finding)
