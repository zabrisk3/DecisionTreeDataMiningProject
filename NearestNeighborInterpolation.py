import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

### 3. This fills in blanks spots in columns using nearest neighbor interpolation

trainingFrame=pd.read_csv('trainingModified.csv')
bigFrame=pd.read_csv('combinedFramebinarized.csv')
numOfRows=len(bigFrame.index)
goodRows=[]
badRows=[]

for r in xrange(numOfRows):
    isComplete=True
    for i in bigFrame.columns.values:
        if (str(bigFrame[i][r])=='nan') or (str(bigFrame[i][r]).lower()=='na') or (str(bigFrame[i][r])==""):
            isComplete=False
            break
    if isComplete:
        goodRows.append(r)
    else:
        badRows.append(r)

goodData=bigFrame.iloc[[k for k in goodRows]]
goodData.to_csv('goodBinarizeddata.csv', index=False)


for j in badRows:
    print(j)
    goodColumns=[]
    badColumns=[]
    for i in bigFrame.columns.values:
        if (str(bigFrame[i][j])=='nan') or (str(bigFrame[i][j]).lower()=='na') or (str(bigFrame[i][j])==""):
            badColumns.append(i)
        else:
            goodColumns.append(i)
    if(len(badColumns) == 0):
        print("Clean")
    else:
        for column in badColumns:
            traininginput=goodData[goodColumns].as_matrix()
            trainingoutput=list(np.ravel(goodData[column].as_matrix()))
            neigh = KNeighborsClassifier(n_neighbors=3)
            neigh.fit(traininginput, trainingoutput)
            values=[]
            for gc in goodColumns:
                values.append(bigFrame[gc][j])
            estimation=neigh.predict([values])[0]
            bigFrame[column][j]=estimation
        print("Done With")
        print(j)

bigFrame.to_csv("cleanedDataFrame.csv", index=False)
goodData=pd.concat([goodData,trainingFrame['responded']],axis=0, ignore_index=True)
goodData.to_csv('binarizedTrainingwithBinarizedresponses.csv', index=False)

print("Done")



