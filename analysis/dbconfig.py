#! /usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

# the database connection, adjust to your local configuration
db = MySQLdb.Connection(host="localhost",  # your host, usually localhost
                        user="root",  # your username
                        passwd="root",  # your password
                        db="acma_cartoon")  # name of the data base
db.set_character_set('utf8')
cursor = db.cursor()


# Load Stopwords
stopwords = []
with open("../assets/stopwords_long.txt") as stopwords_file:
    for line in stopwords_file:
        stopwords.append(line.rstrip())


class CorpusIterator:
    """
    This class is a memory-friendly way to iterate over the database entries matched by an SQL query
    :param query The SQL Query
    :returns entries from the database one by one
    """
    def __init__(self, query):
        self.query = query
        pass

    def __iter__(self):
        cursor.execute(self.query)

        while True:
            row = cursor.fetchone()
            if not row:
                break
            else:
                yield row


def filter_stop_words(word_list, custom_stop_words):
    """
    Filter function to strip stopwords off of a list of words
    :param word_list: list of words to remove stopwords
    :param custom_stop_words: list of custom stop words to filter out
    :return: filtered list of words
    """

    word_list = list(set(word_list).difference(custom_stop_words))

    return list(set(word_list).difference(stopwords))
