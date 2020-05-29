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

# introduce date stamp and archive location for last week's comparison
#

# define a list of stopwords to be excluded from analysis
lst_stop_words = []  # eventually fetch this from a file (json or csv)

# create a list of publications based on the definitions in publications.py
lst_publications = [mod_publications.BBC, mod_publications.Guardian, mod_publications.Independent, mod_publications.Mail, mod_publications.Telegraph, mod_publications.Times, mod_publications.Sun]

mod_processing.fcn_create_archive(str_date_location)

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


################################################################################
# generate a summary instance for the date being considered (s_date_stamp), by combining word_list attributes for each publication
################################################################################

mod_publications.summary_today.att_date_stamp = str_date_stamp
mod_publications.summary_today.att_top_x = int_topx
# concatenate word_lists from individual publications to create a summary
# filter for today, bearing in mind publication instances for last week
mod_publications.summary_today.att_word_list = (
    mod_publications.BBC.att_word_list + \
#    mod_publications.Guardian.att_word_list + \
#    mod_publications.Independent.att_word_list + \
#    mod_publications.Mail.att_word_list + \
    mod_publications.Telegraph.att_word_list + \
    mod_publications.Times.att_word_list + \
    mod_publications.Sun.att_word_list \
    )


# make this processing into functions of summary class
# this will also allow it to be re-used for summary_prev

set_word_set = set(mod_publications.summary_today.att_word_list)

# remove stopwords from the world_list attribute
set_stop_words = mod_stop_words.fcn_stop_words()
set_word_set = set_word_set - set_stop_words

# generate a frequency dictionary by counting occurrences of each word and zipping the list of frequencies together with the word_list

for word in mod_publications.summary_today.att_word_list:  # for each word in the wordlist
    if word in set_word_set:  # if the word is part of the set excluding stopwords
        word_freq = [mod_publications.summary_today.att_word_list.count(p) for p in set_word_set]  # count occurrences
    else:  # otherwise
        pass  # igore the word (as it is a stopword)
freq_dict = dict(list(zip(set_word_set, word_freq)))  # dict of words with frequencies

###############################################################################
# rank words by frequency
#
freqdictrank = [(freq_dict[key], key) for key in freq_dict]
freqdictrank.sort()
freqdictrank.reverse()

# generate a ranking list by selecting top_x words from freq_dict

top_list = freqdictrank[:int_topx]

# repeat the process for last week's date (s_date_stamp-7), by sourcing json publication instances containing wordlists

################################################################################
