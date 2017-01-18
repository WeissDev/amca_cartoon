#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unicodecsv as csv
from bs4 import BeautifulSoup, NavigableString
from mechanize import Browser
from urllib2 import HTTPError
import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="pma",  # your username
                     passwd="admin",  # your password
                     db="acma_cartoon")  # name of the data base
db.set_character_set('utf8')
cursor = db.cursor()


def db_insert(episode_id, position_in_episode, raw_text, speaking_line, raw_character_text, spoken_words, word_count):
    cursor.execute(
        "INSERT INTO southpark_script_lines (episode_id, position_in_episode, raw_text, speaking_line, raw_character_text, spoken_words, word_count) VALUES (%s,%s,%s, %s, %s, %s, %s);",
        (episode_id, position_in_episode, raw_text, speaking_line, raw_character_text, spoken_words, word_count))

    db.commit()


# List of all episodes with names/eipsodenumber and link
completeEpisodeList = dict()

# list of all overview links (pages in forum)
linklist = []

# Browser-initiation to act as normal browser (headers taken from Chrome)
mech = Browser()
mech.set_handle_robots(False)
ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
mech.addheaders = [('User-Agent', ua), ('Accept', '*/*'),
                   ('Referer', 'http://transcripts.foreverdreaming.org/viewforum.php?f=431&start=0')]

# url to overview of all episodes
url = 'http://southpark.wikia.com/wiki/List_of_Episodes'

# open and parse overview of all episodes
overviewPage = mech.open(url)
html = overviewPage.read()
soup = BeautifulSoup(html, 'html.parser')

# find tables containing all links per season and store them into an array (one table per season)
for table in soup.find_all('table',
                           style='width:100%; background:#E7E7E7; font-size:80%; width:100%; border: 1px solid #c3c3c3; border-radius:10px;'):
    for tr in table.find_all('tr', style='text-align:center;'):
        for td in tr.find_all('td', style='font-size:125%'):
            episodeTitle = td.a.string
            episodeLink = 'http://southpark.wikia.com' + td.a.get('href') + '/Script'
            dateTd = td.findNext('td')
            episodeDate = dateTd.string
            episodeSeasonTd = dateTd.findNext('td')
            episodeAndSeasonNumber = episodeSeasonTd.string
            episodeAndSeasonNumber = str(episodeAndSeasonNumber)
            episodeAndSeasonNumber = episodeAndSeasonNumber.replace("\n", "")
            numberTd = episodeSeasonTd.findNext('td')
            episodeNumber = numberTd.string
            linklist.append(episodeLink)
            completeEpisodeList[episodeAndSeasonNumber] = [episodeAndSeasonNumber, episodeNumber, episodeDate,
                                                           episodeTitle, episodeLink]

for episode in completeEpisodeList:
    print('episode: ', completeEpisodeList[episode][3])

for episode in completeEpisodeList:
    #episodeDialogue = []
    try:
        episodePage = mech.open(completeEpisodeList[episode][4])
        html = episodePage.read()
        soup = BeautifulSoup(html, 'html.parser')
    except HTTPError:
        continue

    table = soup.find('table', class_='wikitable')

    try:
        for line_index, tr in enumerate(table.find_all('tr')):
            try:
                actor = tr.th.get_text()
            except AttributeError:
                actor = ''

            try:
                text = tr.td.get_text()
            except AttributeError:
                text = ''

            if actor == '':
                try:
                    db_insert(completeEpisodeList[episode][0], line_index, tr.get_text(), 'false', actor, text, len(text.split()))
                except MySQLdb.Error:
                    print(tr.get_text())
            else:
                try:
                    db_insert(completeEpisodeList[episode][0], line_index, tr.get_text(), 'true', actor, text, len(text.split()))
                except MySQLdb.Error:
                    print(tr.get_text())
                # episodeDialogue.append((actor, text))
        #print('added line with id:', episode[0], line_index)

    except AttributeError:
        #print('episode ', episode[0], 'could not be added')
        continue








# with open('southpark_episodes/' + completeEpisodeList[episode][0] + '.csv', 'wb') as f:  # Just use 'w' mode in 3.x
#        csv_out = csv.writer(f)
#        csv_out.writerow(['actor', 'text'])
#        for row in episodeDialogue:
#            csv_out.writerow(row)


