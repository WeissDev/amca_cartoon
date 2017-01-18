import mechanize
from bs4 import BeautifulSoup
import re
import csv
import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",  # your username
                     passwd="root",  # your password
                     db="acma_cartoon")  # name of the data base


def normalize_line(spoken_line):
    # Remove special characters
    spoken_line = re.sub("[^A-Za-z0-9']+", " ", spoken_line).lower()

    # Remove successive occurrences of same character
    # if more than 3 e.g: aaa => a
    return re.sub(ur"([a-z])\1\1+", r"\1", spoken_line)


def db_insert(season_id, episode_id, position_in_episode, raw_text, raw_character_text, spoken_words, word_count):
    cursor = db.cursor()
    cursor.execute(
        """INSERT INTO southpark_script_lines ( season_id, episode_id, position_in_episode, raw_text, raw_character_text, spoken_words, word_count) VALUES (%s,%s,%s,%s, %s, %s, %s);""",
        (season_id, episode_id, position_in_episode, raw_text, raw_character_text, spoken_words, word_count))
    db.commit()


# id | add season_id | episode_id | raw_text | raw_character_text | spoken_words | word_count
def execute_insert(fname, ep_id):
    with open(fname, "rb") as csvfile:
        pos_in_episode = 0

        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row in csvreader:

            for i, col in enumerate(row):
                row[i] = re.sub("\n", "", col)

            if ep_id == row[1]:
                pos_in_episode += 1
            else:
                ep_id = row[1]
                pos_in_episode = 1
            db_insert(row[0], row[1], pos_in_episode, row[3], row[2], normalize_line(row[3]), len(re.findall(r'\w+', normalize_line(row[3]))))


ep_id = 1
for i in range(1, 20):
    fname = "../SouthParkData/Season-" + str(i) + ".csv"
    execute_insert(fname, ep_id)
