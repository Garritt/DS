import pandas as pd


df = pd.DataFrame.from_csv('celebrity_deaths_2016_id.csv')
refs = {}
black_list = ['and','of','the', 'The', 'for', 'to', 'in', 'from', '&', 'a',
              'at', 'on', 'de', 'My', 'with', 'Who', 'A', 'I', 'Me', 'F',
              'You', 'since', 'All', 'Los', '"(I']
blk_list = set(black_list)
###################################
### Token Reference Observation ###
for index, row in df.iterrows():
    
    about = row['famous_for']
    
    about_str = str(about)
    tokenize = about_str.split()
    for token in tokenize:
 
        if token.startswith("(") or token.endswith(")"):
            continue
        if token in blk_list:
        	continue            
        if refs.get(token) == None:
            refs[token] = 1
        else:
            refs[token]+=1
            print(token,", ",about_str)

## sort by highest reference ##
sortedv = sorted(refs.items(), key=lambda x:x[1], reverse=True)

## Show all token refs -- pick blacklist words ##
#for item in sortedv:
#    print(item)