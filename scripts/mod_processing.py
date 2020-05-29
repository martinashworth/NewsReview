################################################################################
import datetime
import os
import requests
import bs4
import re
import jsonpickle

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


	def fcn_read_html(self):
		with open(f'{str_date_location}/{self.att_name}.html', 'r') as f:
		self.att_html = f.read()


	def fcn_save_html(self, str_date_location):
		'''save contents of publication attribute att_html to filename based on publication attribute att_name and today's archive location (str_date_location)'''

		open(f'{str_date_location}/{self.att_name}.html', 'a').write(self.att_html.text)  # write html to file
		open(f'{str_date_location}/{self.att_name}.html', 'a').close()


	def fcn_parse_html(self):
		# use att_headlines attribute to store text from html response object

		# insert if statement here to see if last 4 chars of att_name are 'prev'
		# then self.att_html = bs4.BeautifulSoup(self.att_html, 'html.parser')

		self.att_html = bs4.BeautifulSoup(self.att_html.text, 'html.parser')

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
				working = str(self.att_headlines[index - 1]).split('subdeck\">')
				# for those items which resulted in a split (ie contained 'article:')
				if len(working) == 2:
					# split the result (where index 1 = text after 'article:')
					working_a = working[1].split('<')
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
	def __init__(self, str_word_list, dct_freq_dict, str_ranked, str_date_stamp, int_top_x, lst_stop_words):
		self.att_word_list = '',
		self.att_freq_dict='',
		self.att_ranked = '',
		self.att_date_stamp = '',
		self.att_top_x = '',
		self.att_stop_words = ''

	# why is this extra-indented?
	def fcn_word_list(self):
		pass # self.word_list = [for all pubs, sum(concat) word_list]


	def fcn_stop_words(self):
		pass # self.word_list = self.word_list - stw


	def fcn_freq_dict(self):
		pass # self.freq_dict = count, zip, then rank each word


	def fcn_top_x(self):
		pass # self.filtered = rank self.freq_dict, filter <= self.top_x

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


def fcn_save_json(ins_publication, str_date_location): # in case change top_x or stw, recreate and save
	json_object = jsonpickle.encode(ins_publication)
	with open(f'{str_date_location}/{ins_publication.att_name}.json', "w") as outfile:
		outfile.write(json_object)

################################################################################
# plotting functionality

def fcn_plot_summary(ins_summary_today, ins_summary_prev, str_today_date):
	pass #


	def fcn_read_summary(self): # read from {summary}_{today/prev}.json
		pass # self.summary_today/prev = {summary}_{today/prev}.json


	def fcn_create_plot(self):
		pass # plt = self.summary_today.filtered v self.summary_prev.filtered


	def fcn_plot_save(plt, today_date):
		pass #

################################################################################
