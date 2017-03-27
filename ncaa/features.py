import pandas as pd
from sklearn import linear_model
from sklearn import metrics, cross_validation

class FeatureModel(object):

	def __init__(self, teams):
		self.teams = teams

	def makeModel(self):
		data = []
		# all teams
		for team in self.teams.keys():
			#print('\n')
			# teams total games
			num_g = self.teams[team]['n_games']
			count = 2	## skip first game
			## get training data
			while count < num_g: # Save last game for round data
				# fv for a game at a point in the
				fv_t = self.featVector(team, count)
				# get same stats for opponent at that matchup.
				# THIS KILLS 75 % OF COLLECTED DATA
				# TRADE OFF FOR OPPONENT FEATURES AT SAME TIME. FOCUS ON MATCHUPS.
				opponent = fv_t[11]
				date = fv_t[12]
				try:
					oppn_count = self.teams[opponent]['games'][team][date]['game_n']
					fv_opp = self.featVector(opponent, oppn_count)
					fv_t = fv_t[1:11]
					fv_opp = fv_opp[1:10]
					###########################
					## BUILD FEATURE SCORE HERE
					###########################
					fv = fv_opp+fv_t
					data.append(fv)
					#print(team, fv_t)
					#print(opponent, fv_opp)
					#print(date, '\n')
				except:
					pass
				count+=1
				

		df = pd.DataFrame(data)
		#print(data)
		describe = df.describe()
		features = list(df.columns[0:18])
		#print(df[features])
		targets = df[18].tolist()
		# Model Creation
		#print('Created Linear Regression Model: ') 
		lgr = linear_model.LogisticRegression(C=1)
		lgr.fit(df[features], targets)
		return lgr
		# print(lgr)
		# cv_pred = cross_validation.cross_val_predict(lgr, df[features], targets, cv=10)
		# print("\n\n", metrics.accuracy_score(targets, cv_pred))
		# print("\n\n", metrics.classification_report(targets, cv_pred))


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

	
	def featVector(self, team, gamen):

		if self.teams[team] is None:
			return None

		maxMargin = 25
		try:
			home_court = self.teams[team]['home_court']
		except:
			home_court = None
		streak = 0

		# Total points and points against
		season_points = 0
		season_points_against = 0
		scr = 0
		scr_a = 0
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
		opponent = None
		date = None
		# create features from extracting from teams dict
		for oppn in opponents:
			matchups = self.teams[team]['games'][oppn].keys()
			for game in matchups:
				court = self.teams[team]['games'][oppn][game]['court']
				game_n = self.teams[team]['games'][oppn][game]['game_n']
				if game_n <= gamen:	# Stopping condition
					scored = self.teams[team]['games'][oppn][game]['scored']
					scored_against = self.teams[team]['games'][oppn][game]['scored_against']
					season_points += scored
					season_points_against += scored_against
					margin = self.__outweighMaxMargin(scored,scored_against, maxMargin)
					if self.teams[team]['games'][oppn][game]['outcome'] is 'W':
						outcome = 1
						if court != home_court:
							away_wins += 1
						wins += 1
					else:
						outcome = 0
						if court != home_court:
							away_losses += 1
						losses += 1
					if game_n >= gamen - 5:
						lfsp += scored
						lfspa += scored_against
						lfmargin += margin
						if self.teams[team]['games'][oppn][game]['outcome'] is 'W':
							lfwins += 1
						else:
							lflosses += 1
					if game_n == gamen:
						streak = self.teams[team]['games'][oppn][game]['curr_streak'].split(" ")
						sign = 0
						if streak[0] is 'W':
							sign = 1
						else:
							sign = -1
						streak = sign * float(streak[1])
						opponent = oppn
						date = game
						scr = scored
						scr_a = scored_against
		
		try:
			wlr = (wins/(losses+wins))
		except ZeroDivisionError:
			wlr = 0
		try:
			lfwlr = (lfwins/(lfwins+lflosses))
		except ZeroDivisionError:
			lfwlr = 0
		try:
			away_score = (away_wins/(away_wins+away_losses))
		except ZeroDivisionError:
			away_score = 0

		

		# vector represents season and recent season statistics up until this gamen. 
		# Outcome then reprsents outcome of gamen.
		return [gamen,wlr,away_score,streak,scr,scr_a,lfwlr,lfsp,lfspa,lfmargin,outcome,opponent,date]
		###########################
		## BUILD FEATURE SCORE HERE
		###########################


		
