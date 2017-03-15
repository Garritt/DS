import os
from pprint import pprint

def extract(filename):

	# keys are stored as alphabatized string -- team1/team2 
	matchups = {}
	teams = {}

	with open(filename, 'r') as data:
		prev_line = None
		for i, line in enumerate(data):
			if line.strip():
				if line.startswith('#'):
					continue

				data_l = line.split(',')
				team = data_l[16].strip()
				opponent = data_l[6]
				date = data_l[1]
				# clean opponent data
				opponent = opponent.split(" ")
				if len(opponent) > 1:
					remove = opponent[-1]
					if remove.startswith('('):
						del opponent[-1]
				opponent = ' '.join(opponent)
				if u'\xa0' in opponent:
					opponent = opponent.split(u'\xa0')[0]

				# submit to teams 
				if teams.get(team) is None:
					try:
						prev_team = prev_line.split(',')[16].strip()
						teams[prev_team]['streak'] = prev_line.split(',')[14].strip()
					except:
						pass				
					teams[team] = {}
					teams[team]['n_games'] = 1
					teams[team]['games'] = {}
					if teams[team]['games'].get(opponent) is None:	
						teams[team]['games'][opponent] = {}
						
				else:
					teams[team]['n_games'] += 1
					if teams[team]['games'].get(opponent) is None:	
						teams[team]['games'][opponent] = {}
					
				teams[team]['games'][opponent][date] = {}
				teams[team]['games'][opponent][date]['outcome'] = data_l[8].strip()
				teams[team]['games'][opponent][date]['point_diff'] = float(data_l[9].strip()) - float(data_l[10].strip())
				teams[team]['games'][opponent][date]['scored'] = float(data_l[9].strip())
				teams[team]['games'][opponent][date]['scored_against'] = float(data_l[10].strip())
				teams[team]['games'][opponent][date]['game_n'] = float(data_l[0])
				
				prev_line = line

	return teams			