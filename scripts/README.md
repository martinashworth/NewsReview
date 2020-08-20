naming conventions
------------------

    objects are named with a prefix to indicate their type:

    att_ = attribute (of a class)
    dct_ = dictionary
    fcn_ = function
    ins_ = instance (of a class)
    int_ = integer
    lst_ = list
    mod_ = module
    set_ = set
    str_ = string

news.py
-------

The main script loads modules and manages program execution:<br />
1) import modules<br />
2) prepare general variables for use during processing<br />
3) create instances of publications<br />
4) for each publication instance, set date, fetch html, save and parse<br />
5) create a Summary instance to bundle results from individual publication instances<br />
6) bundle word_lsits from publication instances into a Summary instance<br />
7) process the Summary to rank words by frequency and store the results<br />
8) call (import) analysis.py

analysis.py
-----------
1) load the Summary instances for the last week
2) calculate the total number of instances for each word over the course of the week, and rank the words by frequency
3) generate a heatmap to show the number of instances for each word, for each day of the last week
<br />
