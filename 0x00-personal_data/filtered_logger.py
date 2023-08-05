#!/usr/bin/env python3
'''using reg ex to filter personal data'''


import re
from typing import List, Any, Match


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    '''defining the function'''
    return re.sub('|'.join('(?<={}=)([^{}]*)'.format(item, separator)
                          for item in fields), redaction, message)
