#!/usr/bin/env python3
'''using reg ex to filter personal data'''


import re
from typing import List, Any, Match


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> Match[str]:
    '''defining the function'''
    res = re.sub('|'.join('(?<={}=)([^{}]*)'.format(item, separator)
                          for item in fields), redaction, message)
    return (res)
