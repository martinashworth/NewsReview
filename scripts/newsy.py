################################################################################
# conventions - prefixes indicate the object type - this belongs in a README

# att = attribute (of a class)
# dct = dictionary
# fcn = function
# ins = instance (of a class)
# int = integer
# lst = list
# mod = module
# str = string

################################################################################
import mod_processing
import mod_publications

################################################################################
### prepare general variables for use during processing ###
################################################################################
# set the number of words to be included in the final ranking
int_topx = 10

# set today's date stamp
str_date_stamp = mod_processing.fcn_now_stamp()

# set today's archive location
str_date_location = mod_processing.fcn_archive_location(str_date_stamp)

# introduce date stamp and archive location for last week's comparison
#

# define a list of stopwords to be excluded from analysis
lst_stop_words = []  # eventually fetch this from a file (json or csv)

# create a list of publications based on the definitions in publications.py
lst_publications = [mod_publications.BBC, mod_publications.Guardian, mod_publications.Independent, mod_publications.Mail, mod_publications.Telegraph, mod_publications.Times, mod_publications.Sun]

mod_processing.fcn_create_archive(str_date_location)

################################################################################
# for each publication instance, for today's date, fetch, store and archive html

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
    mod_processing.fcn_save_json(ins_publication, str_date_location)

################################################################################
# generate a summary instance for the date being considered (s_date_stamp), by combining word_list attributes for each publication

# remove stopwords from the world_list attribute

# generate a frequency dictionary by counting occurrences of each word and zipping the list of frequencies together with the word_list

# generate a ranking list by selecting top_x words from freq_dict

# repeat the process for last week's date (s_date_stamp-7), by sourcing json publication instances containing wordlists

################################################################################
