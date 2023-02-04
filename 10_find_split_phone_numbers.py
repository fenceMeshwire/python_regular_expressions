#!/usr/bin/env python3

# Python 3.9.5

# Dependency
import re

# Used method
# match()           returns the matches in a tuple, following the regular expression's pattern.

phone_code = r'([+][\d]{1,2})-([\d*]+)-([\d*]+)-([\d*]+)'

reg_ex = re.compile(phone_code, flags=re.IGNORECASE)
matches = reg_ex.match('+01-234-567-89000')

try:
    print(matches.groups()) # ('+01', '234', '567', '89000')

    overall_match = matches.group(0)
    country_code = matches.group(1)
    area_code = matches.group(2)
    telephone_prefix = matches.group(3)
    line_number = matches.group(4)

    print(overall_match)        # ('+01', '234', '567', '89000')
    print(country_code[1:])     # 01
    print(area_code)            # 234
    print(telephone_prefix)     # 567
    print(line_number)          # 89000

except AttributeError:
    print('Mismatch for the phone number.')
    print('Please check the input.')
