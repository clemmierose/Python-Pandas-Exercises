import pandas as pd
import altair as alt

pokemon = pd.read_csv('data/pokemon.csv')
pokemon = pokemon.loc[ : , 'attack': 'type']

# Make a groupby object on the column type 
# Find the mean value of each column for each pokemon type using .mean() 
# Save the resulting dataframe as type_means

type_means = pokemon.groupby(by='type').mean() 
type_means

# Obtain the mean speed of each pokemon type from the dataframe 
# type_means by using .loc[]
# Save it in an object named mean_speed

mean_speed = type_means.loc[:, 'speed']

# Display it 

mean_speed

# Make a groupby object on the column legendary 
# Find the maximum and minimum value of each column for each legendary groups using 
# .agg() and save the resulting dataframe as legendary_stats

pokemon = pd.read_csv('data/pokemon.csv')
pokemon = pokemon.loc[ : , ['attack',  'defense', 'capture_rt', 'total_bs', 'legendary']]

legendary_stats = pokemon.groupby('legendary').agg(['max', 'min']) 

# Display it 

legendary_stats

# plot altair

pokemon = pd.read_csv('data/pokemon.csv')

pokemon_type = pd.DataFrame(pokemon.groupby('type').mean().loc[:, 'attack'])

pokemon_type = pokemon_type.reset_index()

attack_plot = alt.Chart(pokemon_type, width=500,
                        height=300).mark_bar().encode(x=alt.X('type:N', sort='-y',
        title='Pokemon type'), y=alt.Y('attack:Q',
        title='Mean attack score'
        )).properties(title='Mean attack value among Pokemon types')

attack_plot