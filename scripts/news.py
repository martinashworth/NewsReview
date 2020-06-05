################################################################################
################################ import modules ################################
################################################################################

import mod_processing  # module contains Class and function definitions
import mod_publications  # module contains Publication and Summary instances
import mod_stop_words  # module contains words to be excluded from analysis

################################################################################
############ prepare general variables for use during processing ###############
################################################################################

# set the number of words to be included in the final ranking
int_topx = 15

# set today's date stamp
str_date_stamp = mod_processing.fcn_now_stamp()

# set today's archive location
str_date_location = mod_processing.fcn_archive_location(str_date_stamp)

# create today's archive location
mod_processing.fcn_create_archive(str_date_location)

# introduce date stamp and archive location for last week's comparison
# for now just use hard-coded dates
str_date_stamp_prev = '2020-05-24'

# set prev archive location
str_date_location_prev = mod_processing.fcn_archive_location(str_date_stamp_prev)

# define a list of stopwords (initially empty) to be excluded from analysis
lst_stop_words = []  # eventually fetch this from a file (json or csv)

################################################################################
######## create instances of publications for today and previous date #########
################################################################################

# create a list of today's publications based on definitions in publications.py
lst_publications = [mod_publications.BBC, mod_publications.Guardian, mod_publications.Independent, mod_publications.Mail, mod_publications.Telegraph, mod_publications.Times, mod_publications.Sun]

# create a list of previous publications using definitions in publications.py
lst_publications_prev = [mod_publications.BBC_prev, mod_publications.Guardian_prev, mod_publications.Independent_prev, mod_publications.Mail_prev, mod_publications.Telegraph_prev, mod_publications.Times_prev, mod_publications.Sun_prev]

################################################################################
## for today's publication instances, set date, fetch, store and archive html ##
################################################################################

for ins_publication in lst_publications:

    # 1) assign today's date stamp to the instance
    ins_publication.att_date = str_date_stamp

    # 2) fetch raw html and store as an attribute of the instance
    ins_publication.fcn_fetch_html()

    # 3) save raw html to file as a reference archive
    ins_publication.fcn_save_html(str_date_location)

    # 4) parse raw html to strip words from headlines and store as an attribute
    ins_publication.fcn_parse_html(str_date_stamp)

    # 5) save the publication object in json with its html as an attribute
#    mod_processing.fcn_save_json(ins_publication, str_date_location)

################################################################################
#### for prev publication instances, set previous date, read and parse html ####
################################################################################

for ins_publication in lst_publications_prev:

    # 1) assign today's date stamp to the instance
    ins_publication.att_date = str_date_stamp_prev

    # 2) read raw html from archived file, store as attribute of instance
    ins_publication.fcn_read_html(str_date_location_prev)

    # 3) parse raw html to strip words from headlines and store as an attribute
    ins_publication.fcn_parse_html(str_date_stamp_prev)

################################################################################
##################### process summary instance for today #######################
################################################################################

# set up initial attributes of summary_today instance
mod_publications.Summary_today.att_date_stamp = str_date_stamp
mod_publications.Summary_today.att_top_x = int_topx
# cast to a list as, by default, it keeps creating a tuple
mod_publications.Summary_today.att_word_list = []

for ins_publication in lst_publications:

    mod_publications.Summary_today.att_word_list = mod_publications.Summary_today.att_word_list + ins_publication.att_word_list

mod_publications.Summary_today.fcn_word_list()
mod_publications.Summary_today.fcn_freq_dict()
mod_publications.Summary_today.fcn_top_x(int_topx)
mod_publications.Summary_today.fcn_write_json(str_date_location)

################################################################################
##################### process summary instance for prev ########################
################################################################################

# set up initial attributes of summary_today instance
#mod_publications.Summary_prev.att_date_stamp = str_date_stamp_prev
#mod_publications.Summary_prev.att_top_x = int_topx
# cast to a list as, by default, it keeps creating a tuple
#mod_publications.Summary_prev.att_word_list = []

#for ins_publication in lst_publications_prev:

#    mod_publications.Summary_prev.att_word_list = mod_publications.Summary_prev.att_word_list + ins_publication.att_word_list

#mod_publications.Summary_prev.fcn_word_list()
#mod_publications.Summary_prev.fcn_freq_dict()
#mod_publications.Summary_prev.fcn_top_x(int_topx)

################################################################################
