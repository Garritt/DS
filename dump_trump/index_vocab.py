import json
import sys
from pprint import pprint

def qgram(word, gram_size):
	ret = set()
	word = list(word)
	window_start = 0 - gram_size + 1
	window_end = 0
	while window_start < (len(word)):
		gram = ''
		temp_s = window_start
		temp_e = window_end
		# Go through window
		while temp_s <= window_end:
			if (temp_s < 0) or (temp_s > (len(word)-1)):
				gram += '#'
			else:
				gram += word[temp_s]
			temp_s += 1

		ret.add(gram)
		window_start += 1
		window_end += 1
	return ret


def jaccard(qgram_set1, qgram_set2):

	union = qgram_set1 | qgram_set2
	intersection = qgram_set1 & qgram_set2
	return len(intersection) / len(union)


def sim_score(word1, word2):
	
	q_1 = qgram(word1, 2)
	q_2 = qgram(word2, 2)
	padd = jaccard(q_1, q_2)
	return padd


def construct_index(data, indexed, indexed_nosim):
	count = 0
	for day in data[username].keys():
		tweet_day = day
		for time in data[username][tweet_day].keys():
			tweet = data[username][tweet_day][time]
			words = tweet.split(" ")
			for word in words:
				# if word not found directly, check sim score with other keys
				if indexed.get(word) == None:
					found = False
					for i_word in indexed.keys():
						if sim_score(word, i_word) > .75:
							count += 1
							indexed[i_word]+=1;
							found = True
							break
					if not found:
						indexed[word] = 1
				else:
					indexed[word]+=1;
				if indexed_nosim.get(word) == None:
					indexed_nosim[word] = 1
				else:
					indexed_nosim[word]+=1;
	print ('\n\n\n COUNT: ', count, '\n\n\n')


if __name__ == '__main__':

	username = 'realDonaldTrump'
	if len(sys.argv) == 2:
		username = sys.argv[1]

	with open('tweet_db.json') as datafile:
		data = json.load(datafile)

	indexed = {}
	indexed_nosim = {}
	
	construct_index(data, indexed, indexed_nosim)
	sort_word = sorted(indexed, key=indexed.__getitem__, reverse=True)
	sort_count = sorted(indexed.values(), reverse=True)
	print(list(zip(sort_word, sort_count)))














