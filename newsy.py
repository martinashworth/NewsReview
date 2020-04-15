###############################################################################
# newsy
###############################################################################
# import modules
# how many import and declaration methods are being used here
# is pyplot a function within the module matplotlib?
import matplotlib.pyplot as plt
# import a function from a module
from requests import get
# import multiple functions from a single module, one with a shorthand
from wordcloud import WordCloud, STOPWORDS as STW, ImageColorGenerator
from bs4 import BeautifulSoup
# import a whole module
# import requests
import logging
import datetime
import os
###############################################################################
# create archive folder
arc_dir = f'output/{datetime.date.today()}'
os.mkdir(arc_dir)
###############################################################################
logging.basicConfig(filename=f'{arc_dir}/newsy.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
###############################################################################
stw = set(STW)
stw.add("wabsnazm")
stw.add("Britain")
stw.add("UK")
stw.add("article")
stw.add("best")
stw.add("case")
stw.add("claim")
stw.add("claims")
stw.add("class")
stw.add("eight")
stw.add("femail")
stw.add("find")
stw.add("five")
stw.add("four")
stw.add("home")
stw.add("href")
stw.add("html")
stw.add("inline")
stw.add("itemprop")
stw.add("kicker")
stw.add("make")
stw.add("may")
stw.add("month")
stw.add("n'")
stw.add("need")
stw.add("new")
stw.add("news")
stw.add("nine")
stw.add("nThe")
stw.add("n3")
stw.add("one")
stw.add("people")
stw.add("reveals")
stw.add("review")
stw.add("right")
stw.add("say")
stw.add("says")
stw.add("sciencetech")
stw.add("separator")
stw.add("seven")
stw.add("show")
stw.add("six")
stw.add("span")
stw.add("star")
stw.add("stars")
stw.add("take")
stw.add("ten")
stw.add("three")
stw.add("tight")
stw.add("time")
stw.add("two")
stw.add("url")
stw.add("us")
stw.add("want")
stw.add("will")
stw.add("world")
stw.add("year")
stw.add("years")
###############################################################################
logging.info('Stopwords Processed')
###############################################################################
# The Guardian
###############################################################################
url = 'https://www.theguardian.com/uk'
response_guardian = get(url)
file_guardian = open(f'{arc_dir}/Guardian.html', "a")
file_guardian.write(response_guardian.text)
file_guardian.close()
logging.info('fetched Guardian')
###############################################################################
# The Telegraph
###############################################################################
url = 'https://www.telegraph.co.uk/'
response_telegraph = get(url)
file_telegraph = open(f'{arc_dir}/Telegraph.html', "a")
file_telegraph.write(response_telegraph.text)
file_telegraph.close()
logging.info('fetched Telegraph')
###############################################################################
# The Mail
###############################################################################
url = 'https://www.dailymail.co.uk/home/index.html'
response_mail = get(url)
file_mail = open(f"{arc_dir}/Mail.html", "a")
file_mail.write(response_mail.text)
file_mail.close()
logging.info('fetched Mail')
###############################################################################
# BBC
###############################################################################
url = 'https://www.bbc.co.uk/news'
response_bbc = get(url)
file_bbc = open(f"{arc_dir}/BBC.html", "a")
file_bbc.write(response_bbc.text)
file_bbc.close()
logging.info('fetched BBC')
###############################################################################
# The Sun
###############################################################################
url = 'https://www.thesun.co.uk/news'
response_thesun = get(url)
file_thesun = open(f"{arc_dir}/thesun.html", "a")
file_thesun.write(response_thesun.text)
file_thesun.close()
logging.info('fetched Sun')
###############################################################################
# The Times
###############################################################################
url = 'https://www.thetimes.co.uk/'
response_times = get(url)
file_times = open(f"{arc_dir}/thetimes.html", "a")
file_times.write(response_times.text)
file_times.close()
logging.info('fetched Times')
###############################################################################
# The Independent
###############################################################################
url = 'https://www.independent.co.uk/'
response_independent = get(url)
file_independent = open(f"{arc_dir}/independent.html", "a")
file_independent.write(response_independent.text)
file_independent.close()
logging.info('fetched Independent')
###############################################################################
# parse the responses
###############################################################################
# response_bbc = requests.get('https://www.bbc.co.uk/news', 'html.parser')
bbc_html = BeautifulSoup(response_bbc.text, 'html.parser')
###############################################################################
headlines_bundle_bbc = []
##############################################################################
# top primary headline
headlines_1_1 = bbc_html.find_all(
    'div', class_='gel-layout__item nw-c-top-stories__primary-item gel-3/4@l gel-3/4@xxl nw-o-keyline nw-o-no-keyline@m')
for head in range(len(headlines_1_1)):
    headlines_bundle_bbc.append(headlines_1_1[head].h3.text)
###############################################################################
# top secondary headline
headlines_1_2 = bbc_html.find_all(
    'div', class_='gel-layout__item nw-c-top-stories__secondary-item nw-c-top-stories__secondary-item--1 gel-1/3@m gel-1/4@l nw-o-keyline nw-o-no-keyline@m')
for head in range(len(headlines_1_2)):
    headlines_bundle_bbc.append(headlines_1_2[head].h3.text)
###############################################################################
# secondary headlines
headlines_2 = bbc_html.find_all(
    'div', class_='gel-layout__item nw-c-top-stories__secondary-item gel-1/3@m gel-1/4@l nw-o-keyline nw-o-no-keyline@m')
for head in range(len(headlines_2)):
    headlines_bundle_bbc.append(headlines_2[head].h3.text)
##############################################################################
# tertiary headlines
headlines_3 = bbc_html.find_all(
    'div', class_='gel-layout__item nw-c-top-stories__tertiary-item--4 gel-1/3@m gel-1/4@l gel-1/1@xxl nw-o-keyline nw-o-no-keyline@m nw-o-keyline@xxl')
for head in range(len(headlines_3)):
    headlines_bundle_bbc.append(headlines_3[head].h3.text)
set(headlines_bundle_bbc)
bundle_string = str(set(headlines_bundle_bbc))
###############################################################################
logging.info('processed BBC')
###############################################################################
# generate a worldclound in memory
wordcloud = WordCloud(background_color="white", max_words=30, max_font_size=50,
                      stopwords=stw, contour_width=1, contour_color='steelblue').generate(bundle_string)
logging.info('wordcloud prepared')
###############################################################################
# Display the wordcloud:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig(f'{arc_dir}/newsy.jpg', width=600, height=300, dpi=None, facecolor='w', edgecolor='w',
            orientation='landscape', papertype=None, format=None,
            transparent=False, bbox_inches=None, pad_inches=0.1,
            metadata=None)
logging.info('wordcloud saved')
