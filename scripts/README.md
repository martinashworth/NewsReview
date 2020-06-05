================================================================================
1.  naming conventions
================================================================================

    objects are named with a prefix to indicate their type:

    att = attribute (of a class)
    dct = dictionary
    fcn = function
    ins = instance (of a class)
    int = integer
    lst = list
    mod = module
    set = set
    str = string

================================================================================
2.  main program script and modules
================================================================================

    news.py             main program script
    mod_processing.py   contains Class and function definitions
    mod_publications.py contains Publication and Summary instances
    mod_stop_words.py   contains words to be excluded from analysis

================================================================================
3.  news.py
================================================================================

a.  import modules
------------------

    mod_processing      # module; contains Class and function definitions
    mod_publications    # module; contains Publication and Summary instances
    mod_stop_words      # module; contains words to be excluded from analysis

b.  prepare initial variables for use during processing
-------------------------------------------------------

    int_topx            number of words to be included in the final ranking
    str_date_stamp      date stamp for today; YYYY-MM-DD
    str_date_stamp_prev date stamp for previous period; YYYY-MM-DD
    str_date_location   archive location; uses str_date_stamp as an argument
    lst_stop_words      list of words to be excluded from analysis

c.  create today's archive location
-----------------------------------

i)      call fcn_create_archive(str_date_location) to create the archive location for today's html files

d.  create instances of publications for today and previous date
----------------------------------------------------------------

i)      The Publication class is defined in mod_processing.py with the following attributes:

        att_name        name of the publication
        att_url         url
        att_html        html making up the front page of the publication
        att_word_list   list of words contained in the html
        att_headlines   headlines stored within tags in the html
        att_date_stamp  date stamp, YYY-MM-DD

ii)     Definitions of instances, including urls, for the following publications are stored in mod_publications.py:

        BBC
        Guardian
        Independent
        Mail
        Telegraph
        Times
        Sun

iii)    A list, lst_publications, contains the individual instances of publications



e.  for today's publication instances, set date, fetch, store and archive html
------------------------------------------------------------------------------

i)      assign today's date stamp to the instance
ii)     fetch raw html and store as an attribute of the instance
iii)    save raw html to file as a reference archive
iv)     parse raw html to strip words from headlines and store as an attribute
v)      save the publication object in json with its html as an attribute

c.  define the archive location for the prior period
----------------------------------------------------

i)      call fcn_archive_location(str_date_stamp_prev)

f.  for prev publication instances, set previous date, read and parse html
--------------------------------------------------------------------------

i)      assign date stamp for the prior period to the instance
ii)     read raw html from archived file, store as attribute of instance
iii)    save raw html to file as a reference archive
iv)     parse raw html to strip words from headlines and store as an attribute
v)      save the publication object in json with its html as an attribute

g.  process summary instance for today
--------------------------------------

# set up initial attributes of summary_today instance
concatenate word lists from publications
mod_publications.Summary_today.fcn_word_list()
mod_publications.Summary_today.fcn_freq_dict()
mod_publications.Summary_today.fcn_top_x(int_topx)

h.  process summary instance for prev
--------------------------------------


================================================================================
4.  mod_processing.py
================================================================================

class Publication():
	'''Publication Class used to describe a publication'''

def fcn_fetch_html(self):
	'''Fetch the html for the url attribute and update the html attribute with the response'''

def fcn_read_html(self, str_date_location):
	'''Read html from archived file, based on self.att_name in str_date_location'''




================================================================================
5.  mod_publications.py
================================================================================


================================================================================
6.  mod_stop_words.py
================================================================================
