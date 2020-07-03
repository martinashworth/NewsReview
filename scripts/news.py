#! /usr/local/bin/python3
################################################################################
# 1 - import modules ###########################################################
################################################################################

import mod_processing  # 1.1 - module contains Class and function definitions
import mod_publications  # 1.2 - module contains Publication & Summary instances
import mod_stop_words  # 1.3 - module contains words to exclude from analysis

################################################################################
# 2 - prepare general variables for use during processing ######################
################################################################################

# 2.1 - set the number of words to be included in the final ranking
int_topx = 15

# 2.2 - define today's date stamp
str_date_stamp = mod_processing.fcn_now_stamp()

# 2.3 - define today's archive location
str_date_location = mod_processing.fcn_archive_location(str_date_stamp)

# 2.4 - create today's archive location
mod_processing.fcn_create_archive(str_date_location)

# 2.5 - define a list of stopwords (initially empty) to exclude from analysis
lst_stop_words = []  # eventually fetch this from a file (json or csv)

################################################################################
# 3 - create instances of publications #########################################
################################################################################

# 3.1 - create a list of publications based on definitions in publications.py
lst_publications = [mod_publications.BBC, mod_publications.Guardian, mod_publications.Independent, mod_publications.Mail, mod_publications.Telegraph, mod_publications.Times, mod_publications.Sun]

################################################################################
# 4 - for each publication instance, set date, fetch html, save and parse ######
################################################################################

# 4.1 - for each publication instance in the list:
for ins_publication in lst_publications:

    # 4.1.1 - assign today's date stamp to the instance
    ins_publication.att_date = str_date_stamp

    # 4.1.2 - fetch raw html and store as an attribute of the instance
    ins_publication.fcn_fetch_html()

    # 4.1.3 - save raw html to file as a reference archive
    ins_publication.fcn_save_html(str_date_location)

    # 4.1.4 - parse raw html, strip words from headlines, store as an attribute
    ins_publication.fcn_parse_html(str_date_stamp)

################################################################################
# 5 - create Summary instance to bundle results from publication instances #####
################################################################################

# 5.1 - set up initial attributes of summary_today instance
mod_publications.Summary_today.att_date_stamp = str_date_stamp
mod_publications.Summary_today.att_top_x = int_topx

# 5.2 - cast to a list as, by default, it keeps creating a tuple
mod_publications.Summary_today.att_word_list = []

################################################################################
# 6 - bundle word_lsits from publication instances into a Summary instance #####
################################################################################

# 6.1 - combine the word_lists of individual publications to create a summary
for ins_publication in lst_publications:

    mod_publications.Summary_today.att_word_list = mod_publications.Summary_today.att_word_list + ins_publication.att_word_list

################################################################################
# 7 - process the Summary to rank words by frequency and store the results #####
################################################################################

# 7.1 - filter out stop words
mod_publications.Summary_today.fcn_word_list()

# 7.2 - generate a dictionary of words and their frequencies
mod_publications.Summary_today.fcn_freq_dict()

# 7.3 - generate a list of the top_x words
mod_publications.Summary_today.fcn_top_x(int_topx)

# 7.4 - save the summary in json format
mod_publications.Summary_today.fcn_write_json(str_date_location)

################################################################################
