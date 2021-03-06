NewsReview
==========

Notes
-------

This is a tool to generate a visual representation of the week's news.<br /><br />
It is intended as a whimsical demonstration of the ability to:<br />
a) source data (in this case by scraping it from a variety of websites)<br />
b) perform some analysis on the data<br />
c) present the results in a visual format that is easy to absorb<br />
d) automate the whole process <br /><br />
![Image of NewsReview](http://whatmakesitgo.com/wp-content/uploads/2020/08/Screenshot-2020-08-21-at-16.52.47.png)

It does this using the steps below:<br />
1) scrape news headlines from the following publications:<br />
[The BBC][] <br />
[The Telegraph][] <br />
[The Times][] <br />
[The Sun][] <br />

[The BBC]: https://www.bbc.co.uk/news
[The Times]: https://www.thetimes.co.uk/
[The Telegraph]: https://www.telegraph.co.uk/
[The Sun]: https://www.thesun.co.uk/news
[scripts]: https://github.com/martinashworth/news/tree/master/scripts
[news.py]: https://github.com/martinashworth/news/blob/master/scripts/news.py
[mod_processing.py]: https://github.com/martinashworth/news/blob/master/scripts/mod_processing.py
[mod_publications.py]: https://github.com/martinashworth/news/blob/master/scripts/mod_publications.py
[mod_stop_words.py]: https://github.com/martinashworth/news/blob/master/scripts/mod_stop_words.py

2) perform analysis in order to extract individual words from headlines then rank the frequency of the words for each day<br /><br />
![Image of DataFrameDay](http://whatmakesitgo.com/wp-content/uploads/2020/08/Screenshot-2020-08-21-at-16.51.34.png)<br />
3) rank the individual words by their total number of appearances over the last week<br /><br />
![Image of DataFrameWeek](http://whatmakesitgo.com/wp-content/uploads/2020/08/Screenshot-2020-08-21-at-16.52.25.png)


Naming Conventions
------------------

Object names are given the following prefixes in order to identify their type: <br />

att_ = attribute (of a class) <br />
dct_ = dictionary <br />
fcn_ = function <br />
ins_ = instance (of a class) <br />
int_ = integer <br />
lst_ = list <br />
mod_ = module <br />
set_ = set <br />
str_ = string <br />


How It Works
------------

The program is managed by the main ./scripts/news.py which calls upon additional modules for class and function definitions, as well as for a list of words to be excluded from processing<br />
1) check for archive directories (see checkdir notes below)<br />
2) download front pages from publications<br />
3) parse html to extract news headlines<br />
4) identify individual words<br />
5) rank the words by the number of instances of each word<br />
6) identify the top 15 words for each day<br />
7) save the results to a date-stamped archive directory<br />
8) tabulate the results for the last 7 days<br />
9) rank the words by overall frequency for the week<br />
10) generate a heatmap to display the results in a visual form<br />
11) save the heatmap to today's archive directory<br />

More details can be found in [./scripts/README.md]: https://github.com/martinashworth/news/blob/master/scripts/README.md
