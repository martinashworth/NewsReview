################################################################################
import datetime
import os
from requests import get

# General Admin Functionality

def now_stamp():
    '''Generate a date stamp for the current year, month, day'''
    now_stamp = f'{datetime.date.today()}'
    return now_stamp


def archive_location(now_stamp):
    '''Define an archive location for today's date'''
    archive_location = f'../archive/{now_stamp}'
    return archive_location


def create_archive(archive_location):
    '''Create the archive location'''
    os.mkdir(archive_location)


class Publication():
    '''Publications describe the...'''
    def __init__(self, name, url, html):
        self.name = name
        self.url = url
        self.wordstring = ''  # placeholder
        self.html = ''

    def fetch_html(self, url):
        '''Fetch the html for the given url and return as an object'''
        response = get(url)
        #response = 'response_text'
        return response

    def store_html(self, publication, date_time_stamp, archive_location, newsfile):
        '''Store the html for the publication'''
        news_file = f'{archive_location}/{publication.name}.html'
        # news_file = f'../archive/{pub_name}.html'
        save_news = open(news_file, "a")
        save_news.write(publication.html.text)
        save_news.close()
