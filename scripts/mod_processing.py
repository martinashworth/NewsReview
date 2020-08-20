################################################################################
import datetime
import os
import requests
import bs4
import re
import jsonpickle
import mod_stop_words

################################################################################

class Publication():
	'''Publication Class used to describe a publication'''
	def __init__(self, att_name, att_url, att_html, att_headlines, att_word_list, att_date_stamp):
		self.att_name = att_name
		self.att_url = att_url
		self.att_html = ''
		self.att_headlines = ''
		self.att_word_list = ''
		self.att_date_stamp = ''


	def fcn_fetch_html(self):
		'''Fetch the html for the url attribute and update the html attribute with the response'''
		self.att_html = requests.get(self.att_url)
		self.att_html = self.att_html


	def fcn_read_html(self, str_date_location):
		'''Read html from archived file, based on self.att_name in str_date_location'''
		with open(f'{str_date_location}/{self.att_name}.html', 'r') as f:
			self.att_html = f.read().lower()


	def fcn_save_html(self, str_date_location):
		'''save contents of publication attribute att_html to filename based on publication attribute att_name and today's archive location (str_date_location)'''

		open(f'{str_date_location}/{self.att_name}.html', 'a').write(self.att_html.text)  # write html to file
		open(f'{str_date_location}/{self.att_name}.html', 'a').close()


	def fcn_parse_html(self, str_date_stamp):
		# use att_headlines attribute to store text from html response object

		if self.att_date == fcn_now_stamp():  # for today's publications
			# use the .text method
			self.att_html = bs4.BeautifulSoup(self.att_html.text.lower(), 'html.parser')

		else:  # for previous publications, just use att_html without .text
			self.att_html = bs4.BeautifulSoup(self.att_html.lower(), 'html.parser')

		if self.att_name == 'BBC':
			# find <h3> tags (ie containing headlines), store in att_headlines
			self.att_headlines = self.att_html.find_all('h3')
			# create a set to add unique headlines to as they are found
			headlines_set = set()
			# step through the headlines contained in the <h3> tags
			for index, headline in enumerate(self.att_headlines, start=1):
				# headlines are preceded by '...__text">' so split on that
				working = str(self.att_headlines[index - 1]).split('__text\">')
				# for items which resulted in a split (ie contained '__text\">')
				if len(working) == 2:
					# split the result (index 1 => text after '__text\">')
					working_a = working[1].split('<')
					headlines_set.add(working_a[0])
				else:  # if len(working) != 2 then it didn't contain a headline
					pass  # therefore, ignore such a case
			self.att_headlines = headlines_set

		if self.att_name == 'Guardian':
			self.att_headlines = 'Guardian word list'

		if self.att_name == 'Independent':
			self.att_headlines = 'Independent word list'

		if self.att_name == 'Mail':
			self.att_headlines = 'Mail word list'

		if self.att_name == 'Telegraph':
			# find <h3> tags (ie containing headlines), store in att_headlines
			self.att_headlines = self.att_html.find_all('a')
			# create a set to add unique headlines to as they are found
			headlines_set = set()
			# step through the headlines contained in the <h3> tags
			for index, headline in enumerate(self.att_headlines, start=1):
				# headlines are preceded by '...__text">' so split on that
				working = str(self.att_headlines[index - 1]).split('__text\">')
				# for items which resulted in a split (ie contained '__text\">')
				if len(working) == 2:
					# split the result (index 1 => text after '__text\">')
					working_a = working[1].split('<')
					headlines_set.add(working_a[0])
				else:  # if len(working) != 2 then it didn't contain a headline
					pass  # therefore, ignore such a case
			self.att_headlines = headlines_set

		if self.att_name == 'Times':
			# find all <a> tags (ie containing headlines), store in att_headlines
			self.att_headlines = self.att_html.find_all('a')
			# create a set to add unique headlines to as they are found
			headlines_set = set()
			# step through the headlines contained in the h3 tags
			for index, headline in enumerate(self.att_headlines, start=1):
				# headlines are preceded by '...article:' so split on that
				working = str(self.att_headlines[index - 1]).split('article:')
				# for those items which resulted in a split (ie contained 'article:')
				if len(working) == 2:
					# split the result (where index 1 = text after 'article:')
					working_a = working[1].split('\"')
					headlines_set.add(working_a[0])
				else:  # if len(working) != 2 then it didn't contain a headline
					pass  # ignore such a case
			self.att_headlines = headlines_set

		if self.att_name == 'Sun':
			self.att_headlines = self.att_html.find_all('a')
			# create a set to add unique headlines to as they are found
			headlines_set = set()
			# step through the headlines contained in the h3 tags
			for index, headline in enumerate(self.att_headlines, start=1):
				# headlines are preceded by '...article:' so split on that
				working = str(self.att_headlines[index - 1]).split('subdeck\">\n\t\t\t')
				# for those items which resulted in a split (ie contained 'article:')
				if len(working) == 2:
					# split the result (where index 1 = text after 'article:')
					working_a = working[1].split('\t\t<')
					headlines_set.add(working_a[0])
				else:  # if len(working) != 2 then it didn't contain a headline
					pass  # ignore such a case
			self.att_headlines = headlines_set

		self.att_word_list = str(self.att_headlines)
		self.att_word_list = re.compile(r'\W+', re.UNICODE).split(self.att_word_list)

		# clear att_html to allow jsonpickle to complete without recursion error
		# self.att_html = ''

################################################################################

class Summary():
	'''Summary Class used to compare individual instances of Publication Class'''
	def __init__(self, att_word_list, att_word_set, att_freq_dict, att_ranked, att_date_stamp, att_top_x, att_stop_words):
		self.att_word_list = [],
		self.att_word_set = (),
		self.att_freq_dict = '',
		self.att_ranked = '',
		self.att_date_stamp = '',
		self.att_top_x = '',
		self.att_stop_words = ''


	def fcn_word_list(self):
		# self.word_list = [for all pubs, sum(concat) word_list]
		self.att_word_set = set(self.att_word_list)
		self.att_stop_words = mod_stop_words.fcn_stop_words()
		self.att_word_set = self.att_word_set - self.att_stop_words


	def fcn_freq_dict(self):
		# self.freq_dict = count, zip, then rank each word
		for word in self.att_word_list:  # for each word in the wordlist
			if word in self.att_word_set:  # if the word is part of the set excluding stopwords
		  		word_freq = [self.att_word_list.count(p) for p in self.att_word_set]  # count occurrences
			else:  # otherwise
				pass  # igore the word (as it is a stopword)
		self.att_freq_dict = dict(list(zip(self.att_word_set, word_freq)))  # dict of words with frequencies


	def fcn_top_x(self, int_topx):
		#pass # self.filtered = rank self.freq_dict, filter <= self.top_x
		freqdictrank = [(self.att_freq_dict[key], key) for key in self.att_freq_dict]
		freqdictrank.sort()
		freqdictrank.reverse()
		self.att_top_x = freqdictrank[:int_topx]

	### encoding and writing to file

	def fcn_write_json(self, str_date_location):
	    Summary_json = jsonpickle.encode(self)
	    with open (f'{str_date_location}/Summary.json', 'w') as Summary_file:
	        Summary_file.write(Summary_json)

################################################################################
# general admin functionality

def fcn_now_stamp():
    '''\nGenerate a date stamp for the current year-month-day\n'''
    str_now_stamp = f'{datetime.date.today()}'
    return str_now_stamp


def fcn_archive_location(str_date_stamp):
    '''Define an archive location for argument passed as date_stamp'''
    str_archive_location = f'../archive/{str_date_stamp}'
    return str_archive_location


def fcn_create_archive(str_date_location):
    '''Create the archive location'''
    os.mkdir(str_date_location)


### is this (fcn_save_json) necessary? ###

def fcn_save_json(ins_publication, str_date_location): # in case change top_x or stw, recreate and save
	json_object = jsonpickle.encode(ins_publication)
	with open(f'{str_date_location}/{ins_publication.att_name}.json', "w") as outfile:
		outfile.write(json_object)

### reading from file and decoding

def fcn_read_json(str_date_location):
    file = open(f'{str_date_location}/Summary.json', 'r')
    Summary_json = file.read()
    Summary_period = jsonpickle.decode(Summary_json)
    return Summary_period

################################################################################
