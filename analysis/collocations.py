#! /usr/bin/env python
# -*- coding: utf-8 -*-

import dbconfig
import nltk
from nltk.collocations import *


def retrieve_by_grouped_ids(grouped, filter_stop_words, custom_stop_words, freq_filter):

    tokens = []
    for group in grouped:
        data = dbconfig.CorpusIterator("SELECT spoken_words FROM southpark_script_lines WHERE id IN (" + ",".join(map(str, group)) + ");")

        for d in data:
            if filter_stop_words:
                filtered_tokens = dbconfig.filter_stop_words(d[0].split(), custom_stop_words)
            else:
                filtered_tokens = d[0].split()

            tokens = tokens + filtered_tokens

    print "Total tokens loaded: %d" % (len(tokens))
    get_bigrams(tokens, freq_filter, word_filter=None, show_top=10)
    get_trigrams(tokens, freq_filter, word_filter=None, show_top=10)


def get_bigrams(words, freq_filter, word_filter, show_top):
    """
    Finds Bigrams from given words and prints them
    http://www.nltk.org/howto/collocations.html
    :param words: list of words
    :param freq_filter: only show bigrams which occur more often than given value
    :param word_filter: only show bigrams that contain given word
    :param show_top: filter to show only the top n bigrams
    :return:
    """
    bigram_measures = nltk.collocations.BigramAssocMeasures()

    finder = BigramCollocationFinder.from_words(words)
    finder.apply_freq_filter(freq_filter)

    if word_filter:
        # only bigrams that contain word set in word_filter
        finder.apply_ngram_filter(word_filter)

    # print the top n bi-grams with the highest PMI
    print "Bi-grams"
    print finder.nbest(bigram_measures.likelihood_ratio, n=show_top)


def get_trigrams(words, freq_filter, word_filter, show_top):
    """
    Finds Trigrams from given words and prints them
    http://www.nltk.org/howto/collocations.html
    :param words: list of words
    :param freq_filter: only show trigrams which occur more often than given value
    :param word_filter: only show trigrams that contain given word
    :param show_top: filter to show only the top n trigrams
    :return:
    """
    trigram_measures = nltk.collocations.TrigramAssocMeasures()

    finder = TrigramCollocationFinder.from_words(words)
    finder.apply_freq_filter(freq_filter)

    if word_filter:
        # only bigrams that contain word set in word_filter
        finder.apply_ngram_filter(word_filter)

    # print the top n tri-grams with the highest PMI
    print "Tri-grams"
    print finder.nbest(trigram_measures.likelihood_ratio, n=show_top)
