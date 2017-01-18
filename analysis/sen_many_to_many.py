from __future__ import print_function
import sys
import re
from textblob import TextBlob
import dbconfig


series = sys.argv[1]


def update_sentiment(new_polarity, new_subjectivity, sen_triple):
    polarity = sen_triple[0]
    subjectivity = sen_triple[1]
    number_of_lines = sen_triple[2]
    number_of_lines += 1

    new_polarity = (polarity + new_polarity) / number_of_lines
    new_subjectivity = (subjectivity + new_subjectivity) / number_of_lines

    return new_polarity, new_subjectivity, number_of_lines


query = "SELECT raw_character_text FROM "+series+"_script_lines WHERE raw_character_text != 'NULL' GROUP BY raw_character_text ORDER BY COUNT(raw_character_text) DESC LIMIT 20"
dbconfig.cursor.execute(query)
characters = dbconfig.cursor.fetchall()

entities_with_sentiments = {}
for speaker in characters:
    speaker = speaker[0]
    for target in characters:
        target = target[0]
        query = "SELECT raw_character_text,spoken_words FROM "+series+"_script_lines WHERE raw_character_text = \"" + \
                speaker + "\" AND spoken_words REGEXP \"" + target + "\";"
        dbconfig.cursor.execute(query)
        adressed_lines = dbconfig.cursor.fetchall()
        for line in adressed_lines:
            line = line[1]
            # print(speaker, target, line)
            tb_line = TextBlob(line.decode("utf8"))
            if speaker + "->" + target not in entities_with_sentiments:
                entities_with_sentiments[speaker + "->" + target] = (tb_line.sentiment.polarity,
                                                                     tb_line.sentiment.subjectivity,
                                                                     1)
            else:
                entities_with_sentiments[speaker + "->" + target] = update_sentiment(tb_line.sentiment.polarity,
                                                                                     tb_line.sentiment.subjectivity,
                                                                                     entities_with_sentiments[
                                                                                         speaker + "->" + target])
print ("\n")
print ("The following character tuples with sentiments were found\n")
print ('-'*100)
print ("Speaker", " " * 12,'Target', ' '*12, 'Polarity', ' ' * 15, "Subjectivity", ' ' * 10, "Num. of documents", " " * 10)
print ('-'*100)


for key, value in sorted(entities_with_sentiments.items(), key=lambda x: x[1]):
    (speaker, target) = re.split('->', key)
    if value[2] > 5:
        print(" {: <20}{: <20}{: <25}{: <18}{: >12}".format(speaker, target, value[0], value[1], value[2]))
