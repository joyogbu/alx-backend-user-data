#!/usr/bin/env python3
'''using reg ex to filter personal data'''


import re
from typing import List, Any, Match
import logging
import csv
import os
from mysql.connector import (connection)


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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
    logger = logging.getLogger("user_data")
    logger.propagate = False
    logger.setLevel(logging.INFO)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)
    c_format = RedactingFormatter(list(PII_FIELDS))
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)
    return (logger)


def get_db() -> connection.MySQLConnection:
    '''connect to a database'''
    PERSONAL_DATA_DB_USERNAME = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    PERSONAL_DATA_DB_PASSWORD = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    PERSONAL_DATA_DB_HOST = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    PERSONAL_DATA_DB_NAME = os.getenv("PERSONAL_DATA_DB_NAME")
    my_con = connection.MySQLConnection(user=PERSONAL_DATA_DB_USERNAME,
                                        password=PERSONAL_DATA_DB_PASSWORD,
                                        host=PERSONAL_DATA_DB_HOST,
                                        database=PERSONAL_DATA_DB_NAME)
    return (my_con)


def main() -> None:
    '''main funtion to connect to the database'''
    con = get_db()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    logger = get_logger()
    for row in cursor.fetchall():
        fields = map(lambda x: x[0], cursor.description)
        result = ([dict(zip(fields, row))])
        tags = [("{}={}; ").format(k, v) for d in result for k, v in d.items()]
        tag = "".join(tags)
        logger.info(tag)
    cursor.close()
    con.close()


if __name__ == "__main__":
    main()
