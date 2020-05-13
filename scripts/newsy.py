#!/usr/local/bin/python3
###############################################################################
# import custom development module
import newsy_proc

# import general modules -> outsource these components to newsy_proc.py

import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

###############################################################################
# create date-stamped archive directory and capture dirname as a variable

arc_dir = ''
arc_dir = newsy_proc.arc_dir()

###############################################################################
# load list of stopwords

stw = newsy_proc.n_stw()  # use set {stw} to capture returned list of stopwords

###############################################################################
# create a dictionary to hold publication details

pub_dict = {
    'thetimes': ["https://www.thetimes.co.uk/", 'thetimes', 0, set()],
    'bbc': ['https://www.bbc.co.uk/news', 'bbc', 0, set()],
    'guardian': ['https://www.theguardian.com/uk', 'guardian', 0, set()]
}

###############################################################################
# Do The Times
###############################################################################
# fetch the front page

news_times = newsy_proc.get_news('https://www.thetimes.co.uk/')

# archive the front page

newsy_proc.write_news(f'{arc_dir}/thetimes', news_times)  # make generic

# parse thetimes html to retain only the rows that include headlines

headlines_times = newsy_proc.parse_thetimes(news_times)

# add the results to pub_dict

pub_dict['thetimes'][2] = len(headlines_times)
pub_dict['thetimes'][3] = headlines_times

###############################################################################
# Do The BBC
###############################################################################
# fetch the front page

news_bbc = newsy_proc.get_news('https://www.bbc.co.uk/news')

# archive the front page

newsy_proc.write_news(f'{arc_dir}/bbc', news_bbc)  # make generic

# parse bbc html to retain only the rows that include headlines

headlines_bbc = newsy_proc.parse_bbc(news_bbc)
pub_dict['bbc'][2] = len(headlines_bbc)
pub_dict['bbc'][3] = headlines_bbc

###############################################################################
# Do The Guardian
###############################################################################
# fetch the front page

news_guardian = newsy_proc.get_news('https://www.theguardian.com/uk/')

# archive the front page

newsy_proc.write_news(f'{arc_dir}/theguardian', news_guardian)  # make generic

###############################################################################
# Do The Mail
###############################################################################

news_mail = newsy_proc.get_news('https://www.dailymail.co.uk/home/index.html')

# archive the front page

newsy_proc.write_news(f'{arc_dir}/themail', news_mail)  # make generic

###############################################################################
# Do The Telegraph
###############################################################################

news_telegraph = newsy_proc.get_news('https://www.telegraph.co.uk/')

# archive the front page

newsy_proc.write_news(f'{arc_dir}/thetelegraph',
                      news_telegraph)  # make generic

###############################################################################
# Do The Independent
###############################################################################

news_independent = newsy_proc.get_news('https://www.independent.co.uk/')

# archive the front page

newsy_proc.write_news(f'{arc_dir}/theindependent',
                      news_independent)  # make generic

###############################################################################
# Do The Sun
###############################################################################

news_sun = newsy_proc.get_news('https://www.thesun.co.uk/news')

# archive the front page

newsy_proc.write_news(f'{arc_dir}/thesun', news_sun)  # make generic

###############################################################################
