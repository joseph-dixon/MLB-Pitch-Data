import sklearn
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import pandas as pd

#import CSV and drop pitch types with 0% classification success
pitches = pd.read_csv('/Users/josephdixon/Desktop/Data Projects/Pitches/CSVs/transformed_pitches.csv', delimiter = ',')
to_drop = pitches[pitches['Pitch Type'] == 'Cutter'].index
pitches.drop(to_drop, inplace = True)
to_drop = pitches[pitches['Pitch Type'] == 'Splitter'].index
pitches.drop(to_drop, inplace = True)

# assign label and attributes. Avg Spin depresses SVM performance, drop that attribute
x = pitches.drop(['Pitch Type','Avg Spin'], axis=1)
y = pitches['Pitch Type']

# designate training and testing data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.20)

#build SVM
svclassifier = SVC(kernel='rbf')
svclassifier.fit(x_train,y_train)

#evaluate model
y_pred = svclassifier.predict(x_test)
print(classification_report(y_test,y_pred))
