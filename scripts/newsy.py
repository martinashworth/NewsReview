################################################################################
# conventions - prefixes indicate the object type - this belongs in a README
################################################################################

# att = attribute (of a class)
# dct = dictionary
# fcn = function
# ins = instance (of a class)
# int = integer
# lst = list
# mod = module
# set = set
# str = string

################################################################################
import mod_processing
import mod_publications
import mod_stop_words
################################################################################

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
#

# define a list of stopwords (initially empty) to be excluded from analysis
lst_stop_words = []  # eventually fetch this from a file (json or csv)

# create a list of today's publications based on definitions in publications.py
lst_publications = [mod_publications.BBC, mod_publications.Guardian, mod_publications.Independent, mod_publications.Mail, mod_publications.Telegraph, mod_publications.Times, mod_publications.Sun]

# create a list of previous publications using definitions in publications.py

lst_publications_prev = [mod_publications.BBC_prev, mod_publications.Guardian_prev, mod_publications.Independent_prev, mod_publications.Mail_prev, mod_publications.Telegraph_prev, mod_publications.Times_prev, mod_publications.Sun_prev]

################################################################################
# for each publication instance, for today's date, fetch, store and archive html
################################################################################

for ins_publication in lst_publications:

    # 1) assign today's date stamp to the instance
    ins_publication.att_date = str_date_stamp

    # 2) fetch raw html and store as an attribute of the instance
    ins_publication.fcn_fetch_html()

    # 3) save raw html to file as a reference archive
    ins_publication.fcn_save_html(str_date_location)

    # 4) parse raw html to strip words from headlines and store as an attribute
    ins_publication.fcn_parse_html()

    # 5) save the publication object in json with its html as an attribute
#    mod_processing.fcn_save_json(ins_publication, str_date_location)
