#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gensim
from gensim import corpora, models
from nltk import RegexpTokenizer
import nltk
import logging
import dbconfig
import re


logging.basicConfig(filename="logfile", format='%(message)s', level=logging.INFO)


def normalize_line(spoken_line):
    # Remove special characters
    spoken_line = re.sub("[^A-Za-z0-9']+", " ", spoken_line).lower()

    # Remove successive occurrences of same character
    # if more than 3 e.g: aaa => a
    return re.sub(ur"([a-z])\1\1+", r"\1", spoken_line)


# Filters words by their tag
def filter_by_tag(line):
    filtered_words = []
    tokenizer = RegexpTokenizer("\w+")
    for tagged_word in nltk.pos_tag(tokenizer.tokenize(line)):
        if re.match("NN", tagged_word[1]):
            filtered_words.append(normalize_line(tagged_word[0]))

    return filtered_words


def retrieve_by_grouped_ids(grouped, filter_stop_words, custom_stop_words):
    """
    Retrieves spoken words iteratively by id
    :param grouped: A 2D list of grouped id's
    :param filter_stop_words: boolean filters the stopwords if set to True
    """
    docs = []

    for group in grouped:
        dbconfig.cursor.execute("SELECT spoken_words,raw_text FROM southpark_script_lines WHERE id IN (" + ",".join(map(str, group)) + ");")
        rows = dbconfig.cursor.fetchall()

        grouped_words = []
        for row in rows:

            if filter_stop_words:
                filtered = filter_by_tag(row[1])
                filtered = dbconfig.filter_stop_words(filtered, custom_stop_words)

            else:
                filtered = row[0].split()

            for word in filtered:
                grouped_words.append(word)

        # if len(grouped_words) > 50:
        docs.append(grouped_words)

    lda(docs)


def lda(documents):

    dictionary = gensim.corpora.Dictionary(documents)

    id2word = {}
    for word in dictionary.token2id:
        id2word[dictionary.token2id[word]] = word

    corpus = [dictionary.doc2bow(text) for text in documents]

    # now train the model; multicore; numofTopics given;
    # see the id2word param: without it, we do not get the words for showing the topics
    lda = gensim.models.ldamulticore.LdaMulticore(corpus,
                                                iterations=50,
                                                passes=10, # since we do not get many documents
                                                num_topics=5,
                                                workers=4,
                                                id2word=dictionary)   # 100 topics is default, change with num_topics=10
    print(lda)

    """
    print("TOP TOPICS")
    for i,topic in enumerate(lda.show_topics(formatted=True, num_words=20, num_topics=10)):
        print("Topic " + str(i+1))
        print(topic)
    """

    # version without weights
    mylist_of_topics_and_words = []

    # if we want just the words per topic:
    for topic in lda.show_topics(formatted=False, num_words=20, num_topics=10):
        (topic_nr, list_of_words_with_weight_tuples) = topic

        # print("topic_nr:", topic_nr)
        # print("topic_word_weight_list:", list_of_words_with_weight_tuples)
        topic_words_joined_as_string = ", ".join([word_weight_tuple[0] for word_weight_tuple in list_of_words_with_weight_tuples])
        # print("topic words as strings:", topic_words_joined_as_string)
        # we store just the list of words, concatenated with comma:
        mylist_of_topics_and_words.append(topic_words_joined_as_string)

    print("FINISHED:")
    print("Topic model with 5 top words per topic looks like:")

    for index, topic_as_string in enumerate(mylist_of_topics_and_words):
        print("\t".join([str(index+1), topic_as_string]))

