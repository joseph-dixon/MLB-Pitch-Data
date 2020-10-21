import csv
import pandas as pd

# initialize labels
column_names = ['Pitch Type','Avg Speed','Avg Spin','Avg Horizontal Break','Avg Vertical Break']

#empy list of lists to write to df
df_elements = []

with open('/Users/josephdixon/Desktop/Data Projects/Pitches/pitches.csv') as csv_file:
    pitches = csv.reader(csv_file)
    header = True

    for row in pitches:
        # skip header
        if header == True:
            header = False
            continue

        else:

            #append pitch instances

            if row[3] != '':
                df_elements.append(['4-Seam',row[3],row[4],row[5],row[6]])
            if row[7] != '':
                df_elements.append(['Slider',row[7],row[8],row[9],row[10]])
            if row[11] != '':
                df_elements.append(['Changeup',row[11],row[12],row[13],row[14]])
            if row[15] != '':
                df_elements.append(['Curveball',row[15],row[16],row[17],row[18]])
            if row[19] != '':
                df_elements.append(['Sinker',row[19],row[20],row[21],row[22]])
            if row[23] != '':
                df_elements.append(['Cutter',row[23],row[24],row[25],row[26]])
            if row[27] != '':
                df_elements.append(['Splitter',row[27],row[28],row[29],row[30]])

df = pd.DataFrame(df_elements, columns = column_names)
df.to_csv('/Users/josephdixon/Desktop/Data Projects/Pitches/transformed_pitches.csv',index=False)
