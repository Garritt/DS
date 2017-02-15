################################

# import pandas as pd

# df = pd.DataFrame.from_csv('../data/csv/celebrity_deaths_2016.csv')

# ID = []
# count = 1

# for index, row in df.iterrows():
# 	ID.append(count)
# 	count+=1

# #df['ID'] = ID
# df_new = df.drop(labels='ID', axis=1)
# df_new.to_csv('../data/csv/celebrity_deaths_2016.csv')


################################

output = open('celebrity_deaths_2016_id.csv', 'w')
output.write("id,age,birth_year,cause_of_death,death_month,death_year,famous_for,name,nationality,famescore\n")

with open('../data/csv/celebrity_deaths_2016.csv') as data_file:
	
	itr = iter(data_file)
	next(itr)
	count = 1
	for i, line in enumerate(itr):
		output.write(str(count)+","+line)
		count+=1

################################
