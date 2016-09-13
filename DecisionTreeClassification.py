import pandas as pd
from sklearn import tree
import numpy as np
import random

### 4. This creates and trains a Decision Tree

goodFrame=pd.read_csv('binarizedTrainingwithBinarizedresponses.csv')
cleanedFrame=pd.read_csv('cleanedDataFrame.csv')

testing_frame=pd.read_csv('testingCandidateOriginal.csv')

clf=tree.DecisionTreeClassifier()
accuracy=0

while accuracy<0.86:
    goodRows=[]
    numberOfrows=len(goodFrame.index)
    badRows=[x for x in xrange(numberOfrows)]
    for x in xrange(445):
        randint=random.randint(0, 7310)
        while randint in goodRows:
            randint=random.randint(0, 7310)
        goodRows.append(randint)
        badRows.remove(randint) #Hello

    for x in xrange(55):
        randint=random.randint(7310+1, numberOfrows-1)
        while randint in goodRows:
            randint=random.randint(7310+1, numberOfrows-1)
        goodRows.append(randint) #Here
        badRows.remove(randint)

    random.shuffle(goodRows)
    random.shuffle(badRows)

    goodData=goodFrame.iloc[[k for k in goodRows]].as_matrix()
    goodResponse=goodFrame['responded'].iloc[[k for k in goodRows]].as_matrix()
    traininginput=cleanedFrame.iloc[[k for k in goodRows]].as_matrix()
    validationinput=cleanedFrame.iloc[[k for k in badRows]].as_matrix()

    clf.fit(traininginput, list(np.ravel(goodResponse)))
    predictions=clf.predict(validationinput)


    score=0
    for x in xrange(len(badRows)):
        if predictions[x]==goodFrame['responded'][badRows[x]]:
            score+=1
    print("Accuracy")
    accuracy=(score*1.0)/len(badRows)
    print(accuracy)

print("Full Prediction")

transformed_length=len(cleanedFrame.index)
training_length=len(goodFrame.index)


testing_input=cleanedFrame.iloc[[i for i in range(training_length, transformed_length)]].as_matrix()
responses=clf.predict(testing_input)

response_frame=pd.DataFrame({ "Responses": responses})

response_frame=pd.concat([testing_frame,response_frame], axis=1)

response_frame.to_csv("testingWithresponses.csv", index=False)

tree.export_graphviz(clf, out_file="tree.dot")

print("Finished")