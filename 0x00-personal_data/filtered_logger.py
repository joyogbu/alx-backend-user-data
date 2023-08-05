#!/usr/bin/env python3
'''using reg ex to filter personal data'''


import re
from typing import List, Any, Match
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = []

    def format(self, record: logging.LogRecord) -> str:
        for items in self.fields:
            return filter_datum(items, self.REDACTION, record, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''defining the function'''
    return re.sub('|'.join('(?<={}=)([^{}]*)'.format(
              item, separator) for item in fields), redaction, message)
