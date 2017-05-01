## Garritt Moede ##

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
	print(ret)
	return ret


def jaccard(qgram_set1, qgram_set2):

	union = qgram_set1 | qgram_set2
	intersection = qgram_set1 & qgram_set2
	return len(intersection) / len(union)


def sim_score(word1, word2, flag):
	
	q_1 = qgram(word1, 2)
	q_2 = qgram(word2, 2)
	if flag == "jacc":
		return jaccard(q_1, q_2)


