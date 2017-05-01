import pandas as pd
import json
import sim_score_lib as jacc
from pprint import pprint

connotation = 'connotation.csv'
tweet_db = 'tweet_db.json'

class structs (object):


	def __init__(self, username):
		with open(tweet_db) as datafile:
			data = json.load(datafile)
		self.tweet_dict = data
		self.pos = {}
		self.neg = {}
		self.overlap_p = {}
		self.overlap_n = {}
		self.count = {}
		self.sort_count = []
		self.username = username

	
	def construct_overlap_index(self):
		pass  # TODO


	def construct_word_index(self):
		
		df = pd.DataFrame.from_csv(connotation)
		
		for index, row in df.iterrows():
			tagP = row['Positiv']
			tagN = row['Negativ']
			if tagP == 'Positiv':
				word = index
				if '#' in word:
					word = word.split('#')[0]
				self.pos[word.lower()] = 0
			elif tagN == 'Negativ':
				word = index
				if '#' in word:
					word = word.split('#')[0]
				self.neg[word.lower()] = 0


	def construct_count_index(self, sim_score):
		
		for day in self.tweet_dict[self.username].keys():
			tweet_day = day
			for time in self.tweet_dict[self.username][tweet_day].keys():
				tweet = self.tweet_dict[self.username][tweet_day][time]['text']
				words = tweet.split(" ")
				for word in words:
					# if word not found directly, check sim score with other keys
					if sim_score:
						if self.count.get(word) == None:
							found = False
							for i_word in self.count.keys():
								if jacc.sim_score(word, i_word, "jacc") > .75:
									count += 1
									self.count[i_word]+=1;
									found = True
									break
							if not found:
								self.count[word] = 1
						else:
							self.count[word]+=1;
					else:	
						if self.count.get(word) == None:
							self.count[word] = 1
						else:
							self.count[word]+=1;
		
		sort_word = sorted(self.count, key=self.count.__getitem__, reverse=True)
		sort_count = sorted(self.count.values(), reverse=True)	
		self.sort_count = list(zip(sort_word, sort_count))


