#!/usr/bin/env python3

# Python 3.9.5

# 08_compile_match.py

# Dependency
import re

number = '491920'
regex = '\d+'

digits = re.compile(regex)
result = digits.match(number)

if result is not None:
  print(result)
