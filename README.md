News
====

Notes
-----

This is a naive beginner's first attempt at:<br />
1) writing a program in Python<br />
2) working with Git<br />
<br />
As such, the approach may appear unorthodox or simply 'wrong', in which case constructive comments are welcome.

Purpose
-------

This is a tool to scrape news headlines from the following publications, and then to perform analysis in order to extract words from the headlines, and rank the words by frequency: <br />
<br />
[The BBC][] <br />
[The Guardian][] <br />
[The Independent][] <br />
[The Mail][] <br />
[The Telegraph][] <br />
[The Times][] <br />
[The Sun][] <br />

[The BBC]: https://www.bbc.co.uk/news
[The Times]: https://www.thetimes.co.uk/
[The Guardian]: https://www.theguardian.com/uk/
[The Mail]: https://www.dailymail.co.uk/home/index.html
[The Telegraph]: https://www.telegraph.co.uk/
[The Independent]: https://www.independent.co.uk/
[The Sun]: https://www.thesun.co.uk/news
[scripts]: https://github.com/martinashworth/news/tree/master/scripts
[news.py]: https://github.com/martinashworth/news/blob/master/scripts/news.py
[mod_processing.py]: https://github.com/martinashworth/news/blob/master/scripts/mod_processing.py
[mod_publications.py]: https://github.com/martinashworth/news/blob/master/scripts/mod_publications.py
[mod_stop_words.py]: https://github.com/martinashworth/news/blob/master/scripts/mod_stop_words.py

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

So as to aid my learning, and hopefully to make the code more readable, object names are given the following prefixes in order to identify their type: <br />

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
More details can be found in [./scripts/README.md]: https://github.com/martinashworth/news/blob/master/scripts/README.md


Download
--------
git clone -b 'vX.X' --single-branch --depth 1 https://github.com/martinashworth/news.git
