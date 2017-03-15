
import extract
from Round import Round
from pprint import pprint

init_matchups = ['Villinova~Mount St. Mary\'s', 'Wisconsin~Virginia Tech', 'Virginia~North Carolina-Wilmington'
	, 'Florida~East Tennessee State']


class Bracket(object):

	init_matchups = ['Villinova~Mount St. Mary\'s', 'Wisconsin~Virginia Tech', 'Virginia~North Carolina-Wilmington'
	, 'Floridia~East Tennessee State']


	def __init__(self, rounds, datafile):
		self.rounds = rounds
		self.teams = extract.extract(datafile)

b = Bracket(4, 'tourny_2017.csv')
r = Round(1, init_matchups, b.teams)
r.calc_round()


