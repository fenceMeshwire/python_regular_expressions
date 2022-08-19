#!/usr/bin/env python3

# Python 3.9.5

# 04_non_greedy_matching.py

# Dependency
import re

greedy_matching = re.compile(r'(Go){3,6}?')
result = greedy_matching.search('GoGoGoGoGoGoGoGoGoGo')
result.group()

# 'GoGoGo' -> 3x 'Go'
