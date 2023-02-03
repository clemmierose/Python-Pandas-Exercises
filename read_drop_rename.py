import pandas as pd

url = 'https://raw.githubusercontent.com/UBC-MDS/MCL-DSCI-511-programming-in-python/master/data/pokemon.csv'

# Read in the data from the URL

pokemon_df = pd.read_csv(url)

# Display the first 10 rows

pokemon_df.head(10)

ad in the data from the text file using the full pathway

pokemon_df = pd.read_csv('data/pokemon-text.txt', delimiter=';')

# Display  the first 10 rows
pokemon_df.head(10)


# Read in the data from the Excel file using the full pathway

pokemon_df = pd.read_excel("data/pokemon.xlsx", sheet_name="pokemon")
                        

# Display the first 10 rows

pokemon_df.head(10)




pokemon_sample = pd.read_csv('data/pokemon.csv',
                             nrows=100,
                             usecols=['name', 'total_bs', 'type'])

# Display the dataframe

pokemon_sample

pokemon = pd.read_csv('data/pokemon.csv', nrows=5)

# Rename the column sp_attack to special_a and
# sp_defense to special_d using df.rename() once  
# Save the new dataframe as `pokemon_special`

pokemon_special = pokemon.rename(columns={'sp_attack':'special_a','sp_defense':'special_d'})

# Display the first 5 rows of the dataframe

pokemon_special

# Drop the columns deck_no, capture_rt, and legendary
# Make sure to overwrite the new dataframe to object pokemon

pokemon = pokemon.drop(columns=['deck_no', 'capture_rt', 'legendary'])

# Display the first 5 rows of the dataframe

pokemon

pokemon = pd.read_csv('data/pokemon.csv')

# Create a new column named total_special 
# that is the sum of column sp_attack and sp_defense
# Save it, overwriting the dataframe named pokemon 

pokemon = pokemon.assign(total_special=pokemon['sp_attack'] + pokemon['sp_defense'])
# Display the first 5 rows of the dataframe
pokemon.head(5)


# Create a new dataframe named fire_pokemon containing only the rows of type "fire" 

fire_pokemon = pokemon[pokemon['type'] == 'fire']

# Create a new dataframe named fire_pokemon containing only the rows of type "fire" 

fire_pokemon = pokemon[pokemon['type'] == 'fire']

fire_pokemon.describe() # or shape()

# Filter the dataframe for the pokemon that have attack and
# defense values both greater than 100
# Save this dataframe as an object named mighty_pokemon 

mighty_pokemon = pokemon[(pokemon['attack'] > 100) & (pokemon['defense'] > 100)]

mighty_pokemon

# Which type has the most Pokemon with attack and defense scores greater than 100?
mighty_pokemon = pokemon[(pokemon['attack'] > 100) & (pokemon['defense'] > 100)]

mighty_col = mighty_pokemon['type']

mighty_type = mighty_col.value_counts()

mighty_type

# Create a new column in the dataframe Name the column base_score, 
# by assigning values 500 or greater from the column total_bs
# as 'strong' pokemon and values less than 500 as 'weak' pokemon

pokemon.loc[pokemon['total_bs'] >= 500, 'base_score']  = 'strong'
pokemon.loc[pokemon['total_bs'] < 500, 'base_score']  = 'weak'

# Display the first 10 rows of the dataframe

pokemon.head(10)


# Create an object using single brackets to obtain the column base_score and name it bs_column

bs_column = pd.DataFrame(pokemon['base_score'])

# Plot the object bs_column using .mark_bar() and save this graph as score_plot

score_plot = alt.Chart(bs_column, width=500, height=300).mark_bar().encode(
    x='base_score',
    y='count()')

score_plot