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

The main script loads modules and manages program execution:
    - import modules
    - prepare general variables for use during processing
    - create instances of publications
    - for each publication instance, set date, fetch html, save and parse
    - create Summary instance to bundle results from publication instances
    - bundle word_lsits from publication instances into a Summary instance
    - process the Summary to rank words by frequency and store the results
