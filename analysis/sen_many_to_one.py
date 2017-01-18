from textblob import TextBlob
import sys
import dbconfig

entity = sys.argv[1]


class CorpusIterator:
    def __init__(self, query):
        self.query = query
        pass

    def __iter__(self):

        dbconfig.cursor.execute(self.query)
        while True:
            row = dbconfig.cursor.fetchone()
            if not row:
                break
            else:
                yield row


def update_sentiment(new_polarity, new_subjectivity, sen_quadruple, current_line):
    polarity = sen_quadruple[0]
    subjectivity = sen_quadruple[1]
    number_of_lines = sen_quadruple[2]
    max_negative_line = sen_quadruple[3]
    number_of_lines += 1

    if new_polarity < polarity:
        max_negative_line = current_line

    new_polarity = (polarity + new_polarity) / number_of_lines
    new_subjectivity = (subjectivity + new_subjectivity) / number_of_lines

    return new_polarity, new_subjectivity, number_of_lines, max_negative_line


def calculate_sentiment(documents):
    # polarity | subjectivity | number of sentiments | max negative line
    entities_with_sentiments = {}
    for doc in documents:
        tb_line = TextBlob(doc[1].decode("utf8"))
        if doc[0] not in entities_with_sentiments:
            entities_with_sentiments[doc[0]] = (tb_line.sentiment.polarity,
                                                tb_line.sentiment.subjectivity,
                                                1,
                                                doc[1].decode("utf8"))
        else:
            entities_with_sentiments[doc[0]] = update_sentiment(tb_line.sentiment.polarity,
                                                                tb_line.sentiment.subjectivity,
                                                                entities_with_sentiments[doc[0]],
                                                                doc[1].decode("utf8"))

    pretty_print(entities_with_sentiments)


def pretty_print(entities_with_sentiments):
    print "\n"
    print "The following entities with sentiments towards " + entity + " were found\n"
    print '-'*100
    print "Entity", " " * 12, 'Polarity', ' ' * 15, "Subjectivity", ' ' * 10, "Num. of documents", " " * 10
    print '-'*100

    for key, value in entities_with_sentiments.iteritems():

        print " {: <20}{: <25}{: <18}{: >12}".format(key, value[0], value[1], value[2])

    print "\n"
    for key, value in entities_with_sentiments.iteritems():
        print str(key) + ": " + value[3] + "\n"


documents = dbconfig.CorpusIterator("SELECT raw_character_text,spoken_words FROM southpark_script_lines WHERE spoken_words REGEXP \" "+ entity+" \";")

calculate_sentiment(documents)

documents = dbconfig.CorpusIterator("SELECT raw_character_text,spoken_words FROM simpsons_script_lines WHERE spoken_words REGEXP \" "+ entity+" \";")

calculate_sentiment(documents)
