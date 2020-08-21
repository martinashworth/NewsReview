News
====

Notes
-------

This is a tool to scrape news headlines from the following publications, and then to perform analysis in order to extract words from the headlines,  rank the words by frequency over the last week, and display the results in a heatmap: <br />
<br />
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

![Image of NewsReview](http://whatmakesitgo.com/wp-content/uploads/2020/08/Screenshot-2020-08-21-at-16.52.47.png)


Directory Structure
--------------

|-archive <br />
| <br />
|-[scripts][] <br />
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- [mod_processing.py][] <br />
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- [mod_publications.py][] <br />
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- [mod_stop_words.py][] <br />
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- [news.py][] <br />
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- [README.md]: https://github.com/martinashworth/news/blob/master/scripts/README.md<br />
| <br />
|-README.md [README.md]: https://github.com/martinashworth/news/blob/master/README.md<br />


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
<br />
More details can be found in [./scripts/README.md]: https://github.com/martinashworth/news/blob/master/scripts/README.md
