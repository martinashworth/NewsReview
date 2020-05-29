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
