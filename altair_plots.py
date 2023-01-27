import pandas as pd
import altair as alt

# Load in the csv named "canucks.csv" the same way you did earlier
# Save it as hockey_players

hockey_players = pd.read_csv('data/canucks.csv', index_col=0)

hockey_players

# Use alt.Chart() to create a chart object, create bar chart of Position column

position_bar = alt.Chart(hockey_players, width=500, height=300).mark_bar(
  color='Teal', opacity=0.5).encode(
  x='Position',
  y='count()').properties(title='Canuck Player Positions')
position_bar


# Plots x as Age and y as Salary using a scatterplot
# Set color to Darkblue and opacity to 0.4
# Don't forget to assign a title as "Canuck players Age vs. Salary"

age_salary_scatter = alt.Chart(hockey_players, width=500, height=300).mark_circle(
  color='Darkblue', opacity=0.4).encode(
  x='Age',
  y='Salary').properties(title='Canuck Players Age vs. Salary')
age_salary_scatter