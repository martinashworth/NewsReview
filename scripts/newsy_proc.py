#!/usr/local/bin/python3
###############################################################################
# module containing functions for analysis and processing of news data
###############################################################################

###############################################################################
# general imports
###############################################################################
from requests import get
from bs4 import BeautifulSoup
from wordcloud import STOPWORDS as STW
import datetime
import os

###############################################################################
# fetch the news and archive it
###############################################################################


def get_news(url):  # given a <url>
    response = get(url)  # fetch the html from <url>
    return response  # return the html as <response>


def write_news(pub_name, pub_news):
    news_file = f'../archive/{pub_name}.html'
    save_news = open(news_file, "a")
    save_news.write(pub_news.text)
    save_news.close()

###############################################################################
# parsing functionality specific to thetimes
###############################################################################


def parse_thetimes(pub_news):
    times_html = BeautifulSoup(pub_news.text, 'html.parser')
    # capture each instance of 'a' tag in an object called 'headlines'
    headlines = times_html.find_all('a')
    # create a set to capture unique headlines
    # print(headlines)
    # return(headlines)
    headlines_times = set()
    for index, headline in enumerate(headlines, start=1):
        # headlines are preceded by '...article:' so split on that
        working = str(headlines[index - 1]).split('article:')
        # for those items which resulted in a split (ie contained 'article:')
        if len(working) == 2:
            # split the result (where index 1 = text after 'article:')
            working_a = working[1].split('\"')
            # index 0 = headline (index 1 = unwanted trailing info)
            # print(working_a[0])
            headlines_times.add(working_a[0])
        else:  # if len(working) != 2 then it didn't contain a headline
            pass  # ignore such a case
    return(headlines_times)


###############################################################################
# parsing functionality specific to bbc
###############################################################################


def parse_bbc(pub_news):
    bbc_html = BeautifulSoup(pub_news.text, 'html.parser')
    # print(bbc_html)
    headlines = bbc_html.find_all('h3')
    headlines_bbc = set()
    for index, headline in enumerate(headlines, start=1):
        # headlines are preceded by '...article:' so split on that
        working = str(headlines[index - 1]).split('__text\">')
        # for those items which resulted in a split (ie contained 'article:')
        if len(working) == 2:
            # split the result (where index 1 = text after 'article:')
            working_a = working[1].split('<')
            # index 0 = headline (index 1 = unwanted trailing info)
            # print(working_a[0])
            headlines_bbc.add(working_a[0])
        else:  # if len(working) != 2 then it didn't contain a headline
            pass  # ignore such a case
    return(headlines_bbc)


###############################################################################
# stopwords
###############################################################################


def n_stw():
    stw = set(STW)
    # stw.add("wabsnazm")
    # stw.add("Britain")
    # stw.add("UK")
    stw.add("")
    stw.add("article")
    stw.add("at")
    stw.add("as")
    stw.add("it")
    stw.add("best")
    stw.add("case")
    stw.add("claim")
    stw.add("claims")
    stw.add("class")
    stw.add("day")
    stw.add("eight")
    stw.add("femail")
    stw.add("find")
    stw.add("first")
    stw.add("five")
    stw.add("four")
    stw.add("go")
    stw.add("going")
    stw.add("home")
    stw.add("href")
    stw.add("html")
    stw.add("inline")
    stw.add("itemprop")
    stw.add("kicker")
    stw.add("ll")
    stw.add("m")
    stw.add("make")
    stw.add("man")
    stw.add("may")
    stw.add("month")
    stw.add("n'")
    stw.add("need")
    stw.add("new")
    stw.add("news")
    stw.add("nine")
    stw.add("now")
    stw.add("nThe")
    stw.add("n3")
    stw.add("of")
    stw.add("one")
    stw.add("people")
    stw.add("put")
    stw.add("reveals")
    stw.add("return")
    stw.add("review")
    stw.add("right")
    stw.add("s")
    stw.add("say")
    stw.add("says")
    stw.add("sciencetech")
    stw.add("separator")
    stw.add("set")
    stw.add("seven")
    stw.add("show")
    stw.add("six")
    stw.add("span")
    stw.add("sport")
    stw.add("star")
    stw.add("stars")
    stw.add("still")
    stw.add("t")
    stw.add("take")
    stw.add("ten")
    stw.add("three")
    stw.add("tight")
    stw.add("time")
    stw.add("times")
    stw.add("top")
    stw.add("two")
    stw.add("url")
    stw.add("us")
    stw.add("want")
    stw.add("will")
    # stw.add("world")
    # stw.add("year")
    # stw.add("years")
    # print(stw)
    return stw

###############################################################################
# create archive folder
###############################################################################


def arc_dir():
    arc_dir = f'../archive/{datetime.date.today()}'
    os.mkdir(arc_dir)
    return arc_dir
###############################################################################
