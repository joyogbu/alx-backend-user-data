#!/usr/bin/env python3
'''using reg ex to filter personal data'''


import re


def filter_datum(fields, redaction, message, separator):
    '''defining the function'''
    # for i in message:
    item = message.split(separator)
    #return (item)
    for i in fields:
        re.sub(i, redaction, message)
