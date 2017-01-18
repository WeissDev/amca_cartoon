import logging
from gensim import corpora, models
import dbconfig
import re

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# Remove special characters
def normalize_line(spoken_line):
    return re.sub("[^A-Za-z0-9']+", " ", spoken_line)


# Filters words by their tag
def filter_by_tag(word, tag):
    query = "SELECT word FROM tagged_words WHERE word=%s AND tag REGEXP %s;"
    dbconfig.cursor.execute(query, (word, tag))

    result = dbconfig.cursor.fetchone()
    if result is not None:
        return result[0]


def retrieve_by_grouped_ids(grouped, filter_stop_words):
    """
    Retrieves spoken words iteratively by id
    :param grouped A 2D list of grouped id's
    :param filter_stop_words boolean filters the stopwords if set to True
    :return: dictionary a gensim.corpora.Dictionary
    """
    dictionary = corpora.Dictionary()
    docs = []

    for group in grouped:
        dbconfig.cursor.execute("SELECT spoken_words,raw_character_text FROM southpark_script_lines WHERE id IN (" + ",".join(map(str, group)) + ");")
        rows = dbconfig.cursor.fetchall()

        grouped_words = []
        for row in rows:

            if filter_stop_words:
                filtered = dbconfig.filter_stop_words(row[0].split(), custom_stop_words=["dad", "penis", "ll", "aghagh"])
            else:
                filtered = row[0].split()

            for word in filtered:
                grouped_words.append((word))

        docs.append(grouped_words)

    dictionary.add_documents(docs)

    print_scores(dictionary, docs)


def print_scores(dictionary, docs):

    dictionary.save("/tmp/tfidf.dict")

    # compile corpus (vectors number of times each elements appears)
    raw_corpus = [dictionary.doc2bow(doc) for doc in docs]

    # store to disk
    corpora.MmCorpus.serialize("/tmp/tfidf.mm", raw_corpus)

    dictionary = corpora.Dictionary.load("/tmp/tfidf.dict")
    corpus = corpora.MmCorpus("/tmp/tfidf.mm")

    # pass MmCorpus to TFIDF model
    tfidf = models.TfidfModel(corpus, normalize=True)

    corpus_tfidf = tfidf[corpus]

    #  Map words id's to their score
    scores = {}
    for doc in corpus_tfidf:
        for id, value in doc:
            word = dictionary.get(id)
            scores[word] = value

    word_count = 0

    for score in sorted(scores.items(), key=lambda x: x[1], reverse=True):

        word_count += 1
        print score[0], score[1]
        if word_count >= 15:
            break

    print "TFIDF: Found " + str(word_count) + " words in " + str(tfidf.num_docs) + " documents"


