from pprint import pprint
from features import FeatureModel


class Round(object):

	def __init__(self, roundnum, matchups, teams):
		self.roundnum = roundnum
		self.matchups = matchups
		self.teams = teams



	def calc_round(self, model):

		fm = FeatureModel(self.teams)
		round_data = []
		nextRound = []
		
		for matchup in self.matchups:
			matchup = matchup.split('~')
			team_a = matchup[0]
			team_b = matchup[1]
			# get last game for this example
			num_g_a = self.teams[team_a]['n_games']
			num_g_b = self.teams[team_b]['n_games']
			# print(num_g_a, num_g_b)
			fv_a = fm.featVector(team_a, num_g_a)[1:10]
			fv_b = fm.featVector(team_b, num_g_b)[1:10]

			## BUILD FEATURE SCORE HERE
			
			fv = fv_b + fv_a
			print(fv)
			#fv_reverse = fv_a + fv_b
			round_data.append(fv)
			#output1 = model.predict(fv)
			#output2 = model.predict(fv_reverse)
			#print(matchup, output1, output2)
		output = model.predict(round_data)
		winners = []
		losers = []
		for idx, win in enumerate(output):
			if win == 1:
				winner = self.matchups[idx].split('~')[0]
				loser = self.matchups[idx].split('~')[1]
			else:
				winner = self.matchups[idx].split('~')[1]
				loser = self.matchups[idx].split('~')[0]
			winners.append(winner)
			losers.append(loser)
			if len(output) is 1:
				return (winners,losers)
		
		## make new round from winners
		count = 0
		while count < len(winners):
			nextRound.append('~'.join([winners[count], winners[count+1]]))
			count += 2
		return (nextRound,losers)

				



