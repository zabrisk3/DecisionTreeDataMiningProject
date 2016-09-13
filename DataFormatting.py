import pandas as pd

### 1. This reformats the spreadsheets. Some columns get deleted, one column is modified
### and both the training and testing spreadhseets are combined.

trainingFrame = pd.read_csv('trainingOriginal.csv')
training_length=len(trainingFrame.index)
training_responses=trainingFrame['responded']


for j in xrange(len(trainingFrame.index)):
        if trainingFrame['responded'][j]=='no':
            trainingFrame['responded'][j]=0
        else:
            trainingFrame['responded'][j]=1

del trainingFrame['id']
del trainingFrame['profit']
trainingFrame.to_csv('trainingModified.csv', index=False)

del trainingFrame['responded']
testingFrame=pd.read_csv('testingCandidateOriginal.csv')
del testingFrame['id']

combined_frame=pd.concat([trainingFrame,testingFrame],axis=0, ignore_index=True)

combined_frame.to_csv("combinedFrame.csv", index=False)

