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
    - import modules<br />
    - prepare general variables for use during processing<br />
    - create instances of publications<br />
    - for each publication instance, set date, fetch html, save and parse<br />
    - create Summary instance to bundle results from publication instances<br />
    - bundle word_lsits from publication instances into a Summary instance<br />
    - process the Summary to rank words by frequency and store the results<br />
