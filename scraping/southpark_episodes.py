import unicodecsv as csv
import mechanize
from bs4 import BeautifulSoup
import re
import csv
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

# All season number hardcoded
season_numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]

episode_wiki_url = "http://southpark.wikia.com/wiki/"

episodate_url = "https://www.episodate.com/tv-show/south-park?season="

season_url = "http://southpark.wikia.com/wiki/Portal:Scripts/Season_"

# wiki_response = br.open(wikipedia_url)
# wiki_html = wiki_response.read()
# wiki_soup = BeautifulSoup(wiki_html, 'html.parser')
# air_dates = wiki_soup.find("table", {"class": "wikitable plainrowheaders wikiepisodetable"})
# print(air_dates)

# id | title | original_air_date | season | number_in_season | number_in_series
number_in_series = 0


def db_insert(id, ep_title, air_date, season_no, no_in_season, no_in_series):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO southpark_episodes (id, title, original_air_date, season, number_in_season, number_in_series) VALUES (%s,%s, %s, %s, %s, %s);""",
                       (id ,ep_title, air_date, season_no, no_in_season, no_in_series))

    db.commit()

for season_index, season in enumerate(season_numbers):
    # print("Season:")
    url = season_url + season
    response = br.open(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    episode_titles = soup.findAll("div", {"class": "lightbox-caption"})

    # Get the air dates
    response = br.open(episodate_url + str(season_index + 1))
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    air_dates = soup.findAll("span", {"class": "episode-date-convert"})

    for episode_index, episode in enumerate(episode_titles):
        air_date = air_dates[episode_index]["data-datetime"].split("T", 1)[0]
        # print(episode_index + 1)
        title = re.sub("[\"]", "", episode.text)
        # print("Number in series:")
        number_in_series += 1
        # print(number_in_series)
        # print(title)
        db_insert(number_in_series, title, air_date, season_index + 1, episode_index + 1, number_in_series)









