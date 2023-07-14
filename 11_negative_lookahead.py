#!/usr/bin/env python3

# Python 3.9.5

# 11_negative_lookahead.py

# Dependency
import re

undesired = re.compile('^(?!.*\d{4}).*$')

samples = ['AB34', '3410']

result = [samples[i] for i in range(len(samples)) if re.match(undesired, samples[i])]

print(result) # ['AB34']
