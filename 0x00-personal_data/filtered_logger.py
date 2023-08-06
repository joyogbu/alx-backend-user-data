#!/usr/bin/env python3
'''using reg ex to filter personal data'''


import re
from typing import List, Any, Match
import logging
import csv


# with open('user_data.csv', 'r') as csvfile:
    # for line in csv.DictReader(csvfile):
        # my_t = tuple([line['phone'], line['ssn'], line['password'],
      #               line['ip'], line['last_login']])
PII_FIELDS = ('email', 'phone', 'ssn', 'password', 'ip')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''defining the function'''
    return re.sub('|'.join('(?<={}=)([^{}]*)'.format(
              item, separator) for item in fields), redaction, message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class that creates a formatter object

    Args:
    -----
    logging.Formater: formatter objectu

    Attributes
    ----------
    REDACTION: a replacement string for the logged message
    FORMAT: format of the log message
    fields: a list of words to be raplaced

    Methods
    -------
    format: a method that returns the formatted log mesage
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """instantiating the class

        Parameters
        ----------
        fields: a list of words
        """
        # super().__init__(self.FORMAT)
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """a function that returns a formatted log

        Parameters
        ----------
        record: a logged message
        """
        # for items in self.fields:
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    '''get logger function that returns a logger'''
    logger = logging.getLogger(__name__)
    # logger = logging.basicConfig(level=logging.INFO)
    logger.propagate = False
    # logger.setLevel(logging.INFO)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)
    c_format = logging.Formatter(RedactingFormatter.FORMAT)
    c_handler.setFormatter(c_format)
    logger.addhandler(c_handler)
    # logger.addHandler(logging.StreamHandler.setFormatter(RedactingFormatter))
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
    return (logger)
