#!/usr/bin/env python3

# Python 3.9.5

# Dependency
import re

output = """Darryl Dixon ddixon@hotmail.com Atlanta,
Richard Grimes rickgrimes01@gmail.com Atlanta,
Carol Peletier carol.peletier@yahoo.com Atlanta,
Maggie Greene mags313@gmail.com n/a
"""

# Used method:
# findall()         returns all matches within a string and returns the matches in a list.
# 
reg_ex_pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
reg_ex = re.compile(reg_ex_pattern, flags=re.IGNORECASE)
result = reg_ex.findall(output)
print(result)
#
# Used method:
# search()          returns a re-object containing information about the location - 
#                   beginning and end - of the expression within the string.
#
fm = reg_ex.search(output)              # fm = first match
result = output[fm.start():fm.end()]    # use the position of beginning and end for locating the 
print(result)                           # search result of the first match within the string.
