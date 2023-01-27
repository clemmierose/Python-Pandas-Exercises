import pandas as pd

# The data

hockey_players = pd.read_csv('data/canucks.csv')
hockey_players

# Selecting only one value using . loc:

# Save Thatcher Demko's salary in an object named demko_paid 

demko_paid = hockey_players.loc[4, 'Salary']
demko_paid

# How old is Zack MacEwen? Save it as object macewen_age

macewen_age = hockey_players.loc[10, 'Age']
macewen_age

# What position does Jacob Markstrom play? Save this as object markstrom_position

markstrom_position = hockey_players.loc[11, 'Position']
markstrom_position

# When was Justin Bailey born? Save it as an object named bailey_birth 

bailey_birth= hockey_players.loc[0, 'Birth Date']
bailey_birth


# Select all the rows from column Salary only 
# Save it as player_cost

player_cost = hockey_players[['Salary']]

# Display it

player_cost

# slice rows and columns using iloc for Jacob Markstrom to Tim Schaller and the columns Player to Height

skilled_players = hockey_players.iloc[11 : 18, 0 : 4]

# Display it

skilled_players

# Slice the rows and columns 
# Save the new dataframe as injured_players

injured_players = hockey_players.iloc[[16,4,21,1], [0,8,7,9]]

# Display it

injured_players

# Sort the hockey_player dataframe by salary in descending order    
# Save it with the name rich_players

rich_players = hockey_players.sort_values(by='Salary', ascending=False)

# Display it
rich_players

# Find the statistics of both categorical and quantitive columns
# Save the dataframe in an object called hockey_stats

hockey_stats = hockey_players.describe(include='all')

# Display it

hockey_stats

# Find the total salary of the team 
# Save it in an object called player_cost

player_cost = hockey_players[['Salary']].sum()

# Display it
player_cost


# Make an object named position_column that consists of just the Position column   

position_column = hockey_players['Position']

# Find the frequencies of the position for the hockey team     
# Save it as position_freq

position_freq = position_column.value_counts()

# Export it to a csv named position_frequencies.csv

position_freq.to_csv('position_frequencies.csv')     

# Don't forget to display it

position_freq