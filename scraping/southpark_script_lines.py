#! /usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
from bs4 import BeautifulSoup
import re
import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",  # your username
                     passwd="root",  # your password
                     db="acma_cartoon")  # name of the data base

# Browser-initiation to act as normal browser (headers taken from Chrome)
br = mechanize.Browser()
br.set_handle_robots(False)
ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
br.addheaders = [('User-Agent', ua), ('Accept', '*/*'),
                   ('Referer', 'http://transcripts.foreverdreaming.org/viewforum.php?f=431&start=0')]

# url to overview of all episodes
episode_overview_url = 'http://southpark.wikia.com/wiki/List_of_Episodes'

# id | episode_id | position_in_episode | raw_text | speaking_line | character_id | (location_id) | raw_character_text |
# (raw_location_text) | spoken_words | word_count

def parse_markup(url):
    response = br.open(url)
    html = response.read()
    return BeautifulSoup(html, 'html.parser')

def db_insert(id, episode_id, position_in_episode, raw_text, raw_character_text, spoken_words, word_count):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO southpark_script_lines (id, episode_id, position_in_episode, raw_text, raw_character_text, spoken_words, word_count) VALUES (%s,%s,%s,%s, %s, %s, %s);""",
                       (id, episode_id, position_in_episode, raw_text, raw_character_text, spoken_words, word_count))

    db.commit()


episode_overview_soup = parse_markup(episode_overview_url)

tables = episode_overview_soup.findAll("table", {"style": "width:100%; background:#E7E7E7; font-size:80%; width:100%; border: 1px solid #c3c3c3; border-radius:10px;"})

db_id = 0
episode_id = 0

for table_index, table in enumerate(tables):
    if table_index > 0:
        tds = table.findAll("td", {"style": "font-size:125%"})

        for tbl_data_index, tbl_data in enumerate(tds):
            script_url = "http://southpark.wikia.com" + tbl_data.a.get("href") + "/Script"
            ep_soup = parse_markup(script_url)
            script_rows = ep_soup.findAll("tr")
            # episode_id
            episode_id += 1
            line_index = 0
            for line in script_rows:
                # print(line)
                line_raw = line.find("span", {"style": "font-size:110%"})

                if line_raw is not None:
                    line_formatted = re.sub(r'\[[^)]*\]', "", line_raw.text)


                   # print(db_id)
                    db_id += 1


                    # position_in_episode
                    line_index += 1
                    # print(line_index)

                    # raw_text
                    # print(line_raw.text)

                    # spoken_words
                    # print(line_formatted)

                    # raw_character_text
                    character_raw = line.find("center").text
                    print(character_raw)

                    # word_count
                    # print(len(re.findall(r'\w+', line_formatted)))
                    print(episode_id)
                    # db_insert(db_id, episode_id, line_index, line_raw.text, character_raw, line_formatted, len(re.findall(r'\w+', line_formatted)))




