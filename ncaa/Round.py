
class Round(object):

	def __init__(self, roundnum, matchups, teams):
		self.roundnum = roundnum
		self.matchups = matchups
		self.teams = teams

	# Computes a score for team a matching up with team b
	# returns a number
	def __score(self, team, opp):
		
		n_games = self.teams[team]['n_games']
		streak = self.teams[team]['streak'].split(" ")
		sign = 0
		if streak[0] is 'W':
			sign = .2
		else:
			sign = -.2
		streak = (sign, streak[1])
		print(streak)

		try:
			prev_matchups = self.teams[team]['games'][opp]	
		except:
			prev_matchups = None

		# Total points and points against
		season_points = 0
		season_points_against = 0
		# season record
		wins = 0
		losses = 0
		# Last five games points and points against
		lfsp = 0
		lfspa = 0
		# Last five games wins and lossses
		lfwins = 0
		lflosses = 0

		opponents = self.teams[team]['games'].keys()
		for oppn in opponents:
			matchups = self.teams[team]['games'][oppn].keys()
			for game in matchups:
				game_n = self.teams[team]['games'][oppn][game]['game_n']
				season_points += self.teams[team]['games'][oppn][game]['scored']
				season_points_against += self.teams[team]['games'][oppn][game]['scored_against']
				if self.teams[team]['games'][oppn][game]['outcome'] is 'W':
					wins += 1
				else:
					losses += 1
				if game_n >= n_games - 5:
					lfsp += self.teams[team]['games'][oppn][game]['scored']
					lfspa += self.teams[team]['games'][oppn][game]['scored_against']
					if self.teams[team]['games'][oppn][game]['outcome'] is 'W':
						lfwins += 1
					else:
						lflosses += 1
		
				
		


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


