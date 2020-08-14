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
<br />
    1) import modules<br />
    2) prepare general variables for use during processing<br />
    3) create instances of publications<br />
    4) for each publication instance, set date, fetch html, save and parse<br />
    5) create Summary instance to bundle results from publication instances<br />
    6) bundle word_lsits from publication instances into a Summary instance<br />
    7) process the Summary to rank words by frequency and store the results<br />
