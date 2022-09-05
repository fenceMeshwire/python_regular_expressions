#!/usr/bin/env python3

# Python 3.9.5

# substitute_rearrange.py

# Dependency
import re

def sub_rearrange_pattern(item):
    pattern = r'(\w+)-(\w+)-(\w+)'
    new_arrangement = r'\3-\1-\2'
    rearranged_item = re.sub(pattern, new_arrangement, item)
    return rearranged_item

if __name__ == '__main__':
    item = '9K1L-3390-20220315'
    rearranged_item = sub_rearrange_pattern(item)
    print('Old part number: ' + str(item))
    print('New part number: ' + str(rearranged_item))
