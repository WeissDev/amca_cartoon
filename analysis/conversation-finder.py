#! /usr/bin/env python
# -*- coding: utf-8 -*-

import dbconfig
import tfidf
import collocations
import lda
import sys
from numpy import array, diff, where, split


def extract_conversation(parent, child):
    """
    Extracts conversations between 2 characters from the database
    :param parent:
    :param child:
    :return: 2D list of database id's grouped by conversations between given characters
    """

    # The dictionary to store all conversations
    conversation = {}

    # These queries retrieve all lines from parent and child respectively
    parent_lines = dbconfig.CorpusIterator(
        "SELECT id,raw_character_text,spoken_words FROM southpark_script_lines WHERE raw_character_text = '" + parent + "'"
    )

    child_lines = dbconfig.CorpusIterator(
        "SELECT id,raw_character_text,spoken_words FROM southpark_script_lines WHERE raw_character_text = '" + child + "'"
    )

    # All lines from the parent are loaded into the dictionary
    for parent_line in parent_lines:
        conversation[parent_line[0]] = (parent_line[1], parent_line[2])

    # ... also all lines from the child
    for child_line in child_lines:
        conversation[child_line[0]] = (child_line[1], child_line[2])

    # This loop removes all lines from the dictionary which are not part of the conversation between the two
    for line_id, spoken_words in sorted(conversation.items(), key=lambda x: int(x[0])):

        next_id = line_id + 1
        prev_id = line_id - 1

        if ((next_id not in conversation) or (conversation[next_id][0] == conversation[line_id][0])) \
                and ((prev_id not in conversation) or (conversation[prev_id][0] == conversation[line_id][0])):

            conversation.pop(line_id)

    # Print the conversations
    conversation_no = 0
    conversation_ids = []
    for line_id, spoken_words in sorted(conversation.items(), key=lambda x: int(x[0])):

        next_id = line_id + 1

        print line_id, spoken_words

        # if the next item does not exist in the conversation dictionary
        # then the current conversation is over
        if next_id not in conversation:
            conversation_no += 1
            print "End conversation", conversation_no

        conversation_ids.append(line_id)

    # create a 2D list with the conversation id's
    return split(conversation_ids, where(diff(conversation_ids) > 2)[0]+1)


grouped_conversation_ids = extract_conversation(sys.argv[1], sys.argv[2])


"""
Retrieve LDA for the given conversations
comment/uncomment line below to print
"""
# lda.retrieve_by_grouped_ids(grouped_conversation_ids, filter_stop_words=True,
#                            custom_stop_words=["mom", "son", "eric", "mommy", "t", " ", "don", "isn", "hey", "huh", "ll"])


"""
Retrieve the TFIDF Scores for the given conversations
comment/uncomment line below to print scores
"""
# tfidf.retrieve_by_grouped_ids(grouped_conversation_ids, filter_stop_words=True)

"""
Retrieve Collocations for the given conversations
comment/uncomment line below to print
"""
collocations.retrieve_by_grouped_ids(grouped_conversation_ids,
                                     filter_stop_words=False,
                                     custom_stop_words=[],
                                     freq_filter=4)







