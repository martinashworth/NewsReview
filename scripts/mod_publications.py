import mod_processing

BBC = mod_processing.Publication(\
    att_name = 'BBC', \
    att_url = 'https://www.bbc.co.uk/news', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Guardian = mod_processing.Publication(\
    att_name = 'Guardian', \
    att_url = 'https://www.theguardian.com/uk', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Independent = mod_processing.Publication(\
    att_name = 'Independent', \
    att_url = 'https://www.independent.co.uk/', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Mail = mod_processing.Publication(\
    att_name = 'Mail', \
    att_url = 'https://www.dailymail.co.uk/home/index.html', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Telegraph = mod_processing.Publication(\
    att_name = 'Telegraph', \
    att_url = 'https://www.telegraph.co.uk/', \
    att_html = '', \
    att_word_list = '', \
    att_headlines = '', \
    att_date_stamp = '')

Times = mod_processing.Publication(\
    att_name = 'Times', \
    att_url = 'https://www.thetimes.co.uk/', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Sun = mod_processing.Publication(\
    att_name = 'Sun', \
    att_url = 'https://www.thesun.co.uk/news', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Summary_today = mod_processing.Summary(\
    str_word_list = '', \
    dct_freq_dict = '', \
    str_ranked = '', \
    str_date_stamp = '', \
    int_top_x = '', \
    lst_stop_words = '')

BBC_prev = mod_processing.Publication(\
    att_name = 'BBC', \
    att_url = '', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Guardian_prev = mod_processing.Publication(\
    att_name = 'Guardian', \
    att_url = '', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Independent_prev = mod_processing.Publication(\
    att_name = 'Independent', \
    att_url = '', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Mail_prev = mod_processing.Publication(\
    att_name = 'Mail', \
    att_url = '', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Telegraph_prev = mod_processing.Publication(\
    att_name = 'Telegraph', \
    att_url = '', \
    att_html = '', \
    att_word_list = '', \
    att_headlines = '', \
    att_date_stamp = '')

Times_prev = mod_processing.Publication(\
    att_name = 'Times', \
    att_url = '', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Sun_prev = mod_processing.Publication(\
    att_name = 'Sun', \
    att_url = '', \
    att_html = '', \
    att_headlines = '', \
    att_word_list = '', \
    att_date_stamp = '')

Summary_prev = mod_processing.Summary(\
    str_word_list = '', \
    dct_freq_dict = '', \
    str_ranked = '', \
    str_date_stamp = '', \
    int_top_x = '', \
    lst_stop_words = '')
