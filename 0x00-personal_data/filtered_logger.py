#!/usr/bin/env python3
'''using reg ex to filter personal data'''


import re


def filter_datum(fields, redaction, message, separator):
    '''defining the function'''
    res = re.sub('|'.join('(?<={}=)([^{}]*)'.format(item, separator)
                          for item in fields), redaction, message)
    return (res)
