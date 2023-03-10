import pandas as pd
import altair as alt

# find mean of calories, sugars and rating for K manufacturer
mfr_k = cereal[cereal['mfr'] == 'K']
csr_df = mfr_k.loc[:, ["calories", "sugars", "rating"]]
cereal_mean = csr_df.mean()
cereal_mean

# or using chaining

cereal_mean = cereal[cereal['mfr'] == 'K'].loc[:,
 ["calories", "sugars", "rating"]].mean()
cereal_mean 


pokemon = pd.read_csv('data/pokemon.csv')

# First, rename the column capture_rt to capture_rate.
# Then, create a new column named AD_total by adding 
# the attack and `defense columns from the pokemon dataset.
# Save this in a dataframe object called plot_df.

plot_df = pd.DataFrame(pokemon.rename(columns={'capture_rt': 'capture_rate'})
                              .assign(AD_total=pokemon['defense'] + pokemon['attack'])
                      )

# Use .mark_circle() to plot AD_total on the x-axis  and capture_rate on the y-axis
# Name the plot pokemon_plot

pokemon_plot = alt.Chart(plot_df, width=500, height=300).mark_circle().encode(
        x='AD_total',
        y='capture_rate')

pokemon_plot