#!/usr/bin/env python3

# Python 3.9.5

# 03_greedy_matching.py

# Dependency
import re

greedy_matching = re.compile(r'(Go){3,6}')
result = greedy_matching.search('GoGoGoGoGoGoGoGoGoGo')
result.group()

# 'GoGoGoGoGoGo' -> 6x 'Go'
