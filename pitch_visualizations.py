import pandas as pd
import plotly.express as px

pitches = pd.read_csv("/Users/josephdixon/Desktop/Data Projects/Pitches/transformed_pitches.csv")
pitches['Avg Horizontal Break'] = pitches['Avg Horizontal Break'].abs()

fig = px.scatter_3d(pitches, x='Avg Speed', y='Avg Horizontal Break', z='Avg Vertical Break',
              color='Pitch Type',size = 'Avg Spin')
fig.show()
