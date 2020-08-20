#! /usr/local/bin/python3
################################################################################
# import modules
################################################################################

import mod_processing  # module contains Class and function definitions
import mod_publications  # module contains Publication & Summary instances
import mod_stop_words  # module contains words to exclude from analysis

################################################################################
# load Summary instances for the last week
################################################################################

from datetime import date, timedelta

Summary0 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today())}'))
Summary1 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+1))}'))
Summary2 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+2))}'))
Summary3 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+3))}'))
Summary4 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+4))}'))
Summary5 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+5))}'))
Summary6 = mod_processing.fcn_read_json(mod_processing.fcn_archive_location(f'{(date.today() - timedelta(days=+6))}'))

################################################################################
import pandas as pd
################################################################################
# create data frames for each day's results
################################################################################

day_frame0 = pd.DataFrame(Summary0.att_top_x).set_index(1)
day_frame1 = pd.DataFrame(Summary1.att_top_x).set_index(1)
day_frame2 = pd.DataFrame(Summary2.att_top_x).set_index(1)
day_frame3 = pd.DataFrame(Summary3.att_top_x).set_index(1)
day_frame4 = pd.DataFrame(Summary4.att_top_x).set_index(1)
day_frame5 = pd.DataFrame(Summary5.att_top_x).set_index(1)
day_frame6 = pd.DataFrame(Summary6.att_top_x).set_index(1)

# create a data frame for the week
frame_week = pd.DataFrame(columns=['Day -6','Day -5','Day -4','Day -3','Day -2','Day -1','Today','tot'],
                          index = list(day_frame6.index.union
                                       (day_frame5.index).union
                                       (day_frame4.index).union
                                       (day_frame3.index).union
                                       (day_frame2.index).union
                                       (day_frame1.index).union
                                       (day_frame0.index)
                                      ))
################################################################################
# process day frames to populate week frame
################################################################################
for w in frame_week.index:

    for d in day_frame0.index:
        if d==w:
            frame_week.loc[w,['Today']]=day_frame0.loc[d,0]

    for d in day_frame1.index:
        if d==w:
            frame_week.loc[w,['Day -1']]=day_frame1.loc[d,0]

    for d in day_frame2.index:
        if d==w:
            frame_week.loc[w,['Day -2']]=day_frame2.loc[d,0]

    for d in day_frame3.index:
        if d==w:
            frame_week.loc[w,['Day -3']]=day_frame3.loc[d,0]

    for d in day_frame4.index:
        if d==w:
            frame_week.loc[w,['Day -4']]=day_frame4.loc[d,0]

    for d in day_frame5.index:
        if d==w:
            frame_week.loc[w,['Day -5']]=day_frame5.loc[d,0]

    for d in day_frame6.index:
        if d==w:
            frame_week.loc[w,['Day -6']]=day_frame6.loc[d,0]

frame_week['tot'] = round(frame_week.sum(axis = 1))

frame_week = frame_week.fillna(0).sort_values(by='tot', ascending=False)

frame_week_tidy = frame_week.drop(columns = ['tot']).head(10)

################################################################################
import matplotlib.pyplot as plt
import seaborn as sns
################################################################################
# generate a heatmap
################################################################################
sns.set()
f, ax = plt.subplots(figsize=(9,6))
sns_plot = sns.heatmap(frame_week_tidy, annot=True, fmt="d", linewidths=.5, ax=ax, cmap="Oranges")

# create a figure from the heatmap and save to file
fig = sns_plot.get_figure()
fig.savefig(f'{mod_processing.fcn_archive_location(date.today())}/heatmap', dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches=None, pad_inches=0.1, metadata=None)

################################################################################
