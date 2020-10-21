import pandas as pd
import plotly.express as px

pitches = pd.read_csv("/Users/josephdixon/Desktop/Data Projects/Pitches/transformed_pitches.csv")
pitches['Avg Horizontal Break'] = pitches['Avg Horizontal Break'].abs()

#random sample of 100 pitches
pitch_sample = pitches.sample(n = 100, replace = False, random_state = 1)

fig = px.scatter_3d(pitch_sample, x='Avg Speed', y='Avg Horizontal Break', z='Avg Vertical Break',
              color='Pitch Type',size = 'Avg Spin')
fig.show()
