#!/usr/bin/env python3

# Python 3.9.5

# 05_matching_order.py

# Dependencies
import re
from datetime import datetime

# Sample text:
text = 'first_text_22-08-2022_text_after_date'

# Construction of the regex pattern:
text_before_pattern = "^(.*?)"
day_pattern = "((0|1|2|3)?\d)-"
month_pattern = "((0|1)?\d)-"
year_pattern = "((20)\d\d)"
text_after_pattern = "(.*?)$"

# Assembly of the regex pattern:
date_pattern = text_before_pattern + day_pattern + \
    month_pattern + year_pattern + text_after_pattern

date_pattern = re.compile(r"" + date_pattern, re.VERBOSE)

# Search the text with the regex pattern:
match_order = date_pattern.search(text)

# Store the results in matching order groups:
text_before = match_order.group(1)
day = match_order.group(2)
month = match_order.group(4)
year = match_order.group(6)
text_after = match_order.group(8)

# Print the result
print(day, month, year)

# Convert the result to a date
str_date = day + '.' + month + '.' + year
date = datetime.strptime(str_date, '%d.%m.%Y')
print(date)
