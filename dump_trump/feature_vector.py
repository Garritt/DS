from structs import structs
import sim_score_lib as jacc

class FeatureVector (object):

	struct = structs('realDonaldTrump')
	struct.construct_word_index()
	#struct.construct_count_index(False)
	#struct.construct_overlap_index()

	def __init__(self, tweet):
		self.text = tweet['text']
		self.favs = tweet['favorites']
		self.rts = tweet['retweets']
		self.created_at = tweet['created_at']
		self.tslt = tweet['time_since_last_tweet']
		scores = self.getPosNegScore(self.text)
		self.pos_score = scores[0]
		self.neg_score = scored[1]
		self.char_count = len(list(list(self.text)))
		self.label = tweet['label']

	def __getPosNegOverlap(self, tweet):
		maxx_p = 0
		maxx_n = 0
		for key, value in struct.overlap_p.items():
			score = jacc.sim_score(tweet, value)
			if score > maxx_p:
				maxx_p = score
		for key, value in struct.overlap_n.items():
			score = jacc.sim_score(tweet, value)
			if score > maxx_n:
				maxx_n = score
		return (maxx_p, maxx_n)		


	def __getPosNegScore(self, tweet):
		count = 0
		found_p = 0
		found_n = 0
		for word in tweet:
			word = word.lower()
			if struct.pos.get(word) != None:
				found_p += 1
			elif struct.neg.get(word) != None:
				found_n += 1
			count += 1
		return ((found_p / count), (found_n / count))

	
	def getFeatureVector(self):
		return list(self.favs, self.rts, self.tslt, self.pos_score, self.neg_score, self.char_count)



