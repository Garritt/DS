from pprint import pprint


class Round(object):

	def __init__(self, roundnum, matchups, teams):
		self.roundnum = roundnum
		self.matchups = matchups
		self.teams = teams
		pprint(self.teams)

		
	def __outweighMaxMargin(self, scored, scored_against, maxMargin):
		sign = 0
		if scored - scored_against > 0:
			sign = 1
		else:
			sign = -1
		if abs(scored - scored_against) > maxMargin:
			return maxMargin * sign
		else:
			return scored - scored_against

	def calc_round(self):

		temp = []
		ret = []
		
		for matchup in self.matchups:
			matchup = matchup.split('~')
			team_a = matchup[0]
			team_b = matchup[1]
			score_a = self.__score(team_a, team_b)
			#score_b = self.__score(team_b, team_a)
			#keep = max(score_a, score_b)
			#temp.append(keep)
		
		count = 0
		while count < len(temp):
			ret.append('~'.join([temp[count], temp[count+1]]))
			count += 2

		return ret


	# Computes a score for team a matching up with team b
	# returns a number
	def __score(self, team, opp):
		maxMargin = 25
		n_games = self.teams[team]['n_games']
		streak = self.teams[team]['streak'].split(" ")
		home_court = self.teams['home_court']
		sign = 0
		if streak[0] is 'W':
			sign = .2
		else:
			sign = -.2
		streak = (sign, streak[1])

		# Total points and points against
		season_points = 0
		season_points_against = 0
		# season record
		wins = 0
		losses = 0
		# season margin. With a max margin of +-25 per game
		margin = 0
		# Margin score of last five games
		lfmargin = 0
		# Last five games points and points against
		lfsp = 0
		lfspa = 0
		# Last five games wins and lossses
		lfwins = 0
		lflosses = 0
		# On road wins and losses
		away_wins = 0
		away_losses = 0

		opponents = self.teams[team]['games'].keys()
		for oppn in opponents:
			matchups = self.teams[team]['games'][oppn].keys()
			for game in matchups:
				court = self.teams[team]['games'][oppn][game]['court']
				game_n = self.teams[team]['games'][oppn][game]['game_n']
				scored = self.teams[team]['games'][oppn][game]['scored']
				scored_against = self.teams[team]['games'][oppn][game]['scored_against']
				margin += self.__outweighMaxMargin(scored,scored_against, maxMargin)
				season_points += scored
				season_points_against += scored_against
				if self.teams[team]['games'][oppn][game]['outcome'] is 'W':
					if court not home_court:
						away_wins += 1
					wins += 1
				else:
					if court not home_court:
						away_losses += 1
					losses += 1
				if game_n >= n_games - 5:
					lfsp += scored
					lfspa += scored_against
					lfmargin += margin
					if self.teams[team]['games'][oppn][game]['outcome'] is 'W':
						lfwins += 1
					else:
						lflosses += 1
		
		try:
			prev_matchups = self.teams[team]['games'][opp]	
		except:
			prev_matchups = None
				



