
import extract
from Round import Round
from pprint import pprint
from features import FeatureModel


class Bracket(object):

	def __init__(self, rounds, datafile):
		self.rounds = rounds
		self.teams = extract.extract(datafile)
		#pprint(self.teams)
		# create log reg model for each team
		self.fm = FeatureModel(self.teams)
		self.model = self.fm.makeModel()
	
	def fillBracket(self):
		
		matchups = ['Villinova~Mount St. Mary\'s', 'Wisconsin~Virginia Tech', 'Virginia~North Carolina-Wilmington'
					,'Florida~East Tennessee State', 'SMU~USC', 'Baylor~New Mexico State', 'South Carolina~Marquette'
					,'Duke~Troy','Kansas~UC-Davis', 'Miami (FL)~Michigan State', 'Iowa State~Nevada', 'Purdue~Vermont'
					,'Creighton~Rhode Island', 'Oregon~Iona', 'Michigan~Oklahoma State', 'Louisville~Jacksonville State'
					,'Gonzaga~South Dakota State', 'Northwestern~Vanderbilt', 'Notre Dame~Princeton', 'West Virginia~Bucknell'
					,'Maryland~Xavier', 'Florida State~Florida Gulf Coast', 'Saint Mary\'s (CA)~Virginia Commonwealth'
					,'Arizona~North Dakota', 'North Carolina~Texas Southern', 'Arkansas~Seton Hall', 'Minnesota~Middle Tennessee'
					, 'Butler~Winthrop', 'Cincinnati~Kansas State', 'UCLA~Kent State', 'Dayton~Wichita State', 'Kentucky~Northern Kentucky']
		
		print('\nRound 1')
		print(matchups)
		count = 1	
		while count <= self.rounds:		# or while len(matchups) == 1 
			r = Round(count, matchups, self.teams)
			calc = r.calc_round(self.model)
			matchups = calc[0]
			losers = calc[1]
			print('losers: ', losers, '\n')
			# update winning team stats based on new round
			loser_idx = 0
			for matchup in matchups:
				matchup = matchup.split('~')
				for team in matchup:
					self.teams[team]['n_games'] += 1
					if self.teams[team]['games'].get(losers[loser_idx]) is None:
						self.teams[team]['games'][losers[loser_idx]] = {}
					self.teams[team]['games'][losers[loser_idx]][count] = {}
					self.teams[team]['games'][losers[loser_idx]][count]['outcome'] = 'W'
					self.teams[team]['games'][losers[loser_idx]][count]['game_n'] = self.teams[team].get('n_games')
					# figure out what to set these values as. This could fuck shit up. All hardcoded crap
					self.teams[team]['games'][losers[loser_idx]][count]['point_diff'] = 5
					self.teams[team]['games'][losers[loser_idx]][count]['scored'] = 80
					self.teams[team]['games'][losers[loser_idx]][count]['scored_against'] = 75
					self.teams[team]['games'][losers[loser_idx]][count]['court'] = 'Neutral' 
					self.teams[team]['games'][losers[loser_idx]][count]['curr_streak'] = 'W '+ str(count * 3)
					loser_idx += 1
			# Printing new matchups every round!
			count += 1
			print('Round', count)
			print(matchups)





b = Bracket(5, 'tourny_2017.csv')
b.fillBracket()

