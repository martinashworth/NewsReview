#! /usr/local/bin/python3
################################################################################
# import modules
################################################################################

import mod_processing  # module contains Class and function definitions
import mod_publications  # module contains Publication & Summary instances
import mod_stop_words  # module contains words to exclude from analysis

################################################################################
# prepare general variables for use during processing
################################################################################

# set the number of words to be included in the final ranking
int_topx = 15

# define today's date stamp
str_date_stamp = mod_processing.fcn_now_stamp()

# define today's archive location
str_date_location = mod_processing.fcn_archive_location(str_date_stamp)

# create today's archive location
mod_processing.fcn_create_archive(str_date_location)

# define a list of stopwords (initially empty) to exclude from analysis
lst_stop_words = []  # eventually fetch this from a file (json or csv)

################################################################################
# create instances of publication classes
################################################################################

# create a list of publications based on definitions in publications.py
lst_publications = [mod_publications.BBC, mod_publications.Guardian, mod_publications.Independent, mod_publications.Mail, mod_publications.Telegraph, mod_publications.Times, mod_publications.Sun]

################################################################################
# for each publication instance, set date, fetch html, save and parse
################################################################################

# for each publication instance in the list:
for ins_publication in lst_publications:

    # assign today's date stamp to the instance
    ins_publication.att_date = str_date_stamp

    # fetch raw html and store as an attribute of the instance
    ins_publication.fcn_fetch_html()

    # save raw html to file as a reference archive
    ins_publication.fcn_save_html(str_date_location)

    # parse raw html, strip words from headlines, store as an attribute
    ins_publication.fcn_parse_html(str_date_stamp)

################################################################################
# create Summary instance to bundle results from publication instances
################################################################################

# set up initial attributes of summary_today instance
mod_publications.Summary_today.att_date_stamp = str_date_stamp
mod_publications.Summary_today.att_top_x = int_topx

# cast to a list as, by default, it keeps creating a tuple
mod_publications.Summary_today.att_word_list = []

################################################################################
# bundle word_lsits from publication instances into a Summary instance
################################################################################

# combine the word_lists of individual publications to create a summary
for ins_publication in lst_publications:

    mod_publications.Summary_today.att_word_list = mod_publications.Summary_today.att_word_list + ins_publication.att_word_list

################################################################################
# process the Summary to rank words by frequency and store the results
################################################################################

# filter out stop words
mod_publications.Summary_today.fcn_word_list()

# generate a dictionary of words and their frequencies
mod_publications.Summary_today.fcn_freq_dict()

# generate a list of the top_x words
mod_publications.Summary_today.fcn_top_x(int_topx)

# save the summary in json format
mod_publications.Summary_today.fcn_write_json(str_date_location)

################################################################################
# put today's Summary into same name format as rest of week
Summary0 = mod_publications.Summary_today

# load Summary instances for the last week
from datetime import date, timedelta
Summary1 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+1))}'))
Summary2 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+2))}'))
Summary3 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+3))}'))
Summary4 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+4))}'))
Summary5 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+5))}'))
Summary6 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+6))}'))

import pandas as pd
# create data frames for each day's results
day_frame0 = pd.DataFrame(Summary0.att_top_x).set_index(1)
day_frame1 = pd.DataFrame(Summary1.att_top_x).set_index(1)
day_frame2 = pd.DataFrame(Summary2.att_top_x).set_index(1)
day_frame3 = pd.DataFrame(Summary3.att_top_x).set_index(1)
day_frame4 = pd.DataFrame(Summary4.att_top_x).set_index(1)
day_frame5 = pd.DataFrame(Summary5.att_top_x).set_index(1)
day_frame6 = pd.DataFrame(Summary6.att_top_x).set_index(1)

# create a data frame for the week
frame_week = pd.DataFrame(columns={0,1,2,3,4,5,6,'tot'},
                          index = list(day_frame0.index.union
                                       (day_frame1.index).union
                                       (day_frame2.index).union
                                       (day_frame3.index).union
                                       (day_frame4.index).union
                                       (day_frame5.index).union
                                       (day_frame6.index)
                                      ))

# process day frames to populate week frame
for w in frame_week.index:

    for d in day_frame0.index:
        if d==w:
            frame_week.loc[w,[0]]=day_frame0.loc[d,0]

    for d in day_frame1.index:
        if d==w:
            frame_week.loc[w,[1]]=day_frame1.loc[d,0]

    for d in day_frame2.index:
        if d==w:
            frame_week.loc[w,[2]]=day_frame2.loc[d,0]

    for d in day_frame3.index:
        if d==w:
            frame_week.loc[w,[3]]=day_frame3.loc[d,0]

    for d in day_frame4.index:
        if d==w:
            frame_week.loc[w,[4]]=day_frame4.loc[d,0]

    for d in day_frame5.index:
        if d==w:
            frame_week.loc[w,[5]]=day_frame5.loc[d,0]

    for d in day_frame6.index:
        if d==w:
            frame_week.loc[w,[6]]=day_frame6.loc[d,0]

frame_week['tot'] = round(frame_week.sum(axis = 1))

frame_week = frame_week.fillna(0).sort_values(by='tot', ascending=False)

frame_week_tidy = frame_week.drop(columns = ['tot']).head(10)


import matplotlib.pyplot as plt
import seaborn as sns

# generate a heatmap
sns.set()
f, ax = plt.subplots(figsize=(9,6))
sns_plot = sns.heatmap(frame_week_tidy, annot=True, fmt="d", linewidths=.5, ax=ax, cmap="Oranges")

# create a figure from the heatmap and save to file
fig = sns_plot.get_figure()
fig.savefig(f'{str_date_location}/heatmap', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        metadata=None)
