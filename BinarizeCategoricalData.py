import pandas as pd

### 2. This converts categorical columns into a series of binary columns

combined_frame=pd.read_csv('combinedFrame.csv')
combined_length=len(combined_frame.index)
categorical_columns=[]

def binarize(dataframe,column_list):

    for i in combined_frame.columns.values:
        is_categorical=False
        for j in xrange(combined_length):
            if (type(combined_frame[i][j]).__name__=='str') and (str(combined_frame[i][j]).lower()!='nan') and (str(combined_frame[i][j]).lower()!='na'):
                print("Here")
                print(combined_frame[i][j])
                is_categorical=True
                break
        if is_categorical:
            categorical_columns.append(i)

    print(categorical_columns)

    length=len(dataframe.index)
    for i in column_list:
        print(i)
        unique_values = nonBlankunique(pd.Series.unique(dataframe[i]))
        n=len(unique_values)
        for z in xrange(n):
            print(z)
            new_column=pd.DataFrame({i+"_"+str(unique_values[z]): [0 for row in xrange(length)]})
            dataframe=pd.concat([dataframe,new_column],axis=1)
            for m in xrange(length):
                print(i)
                print(z)
                print(m)
                if dataframe[i][m]==unique_values[z]:
                    dataframe[i+"_"+ unique_values[z]][m]=1
                if str(dataframe[i][m]=='nan') or (str(dataframe[i][m]).lower()=='na') or (str(dataframe[i][m])==""):
                    dataframe[i+"_"+unique_values[z]][m]=""
        print("Done")
        print(i)
        del dataframe[i]
    return dataframe

def nonBlankunique(array):
    trueUnique=[]
    for j in xrange(len(array)):
        if (type(array[j]).__name__=='str') and (str(array[j]).lower()!='nan') and (str(array[j]).lower()!='na'):
            trueUnique.append(array[j])
    return trueUnique


transformed_matrix=binarize(combined_frame,categorical_columns)
print(transformed_matrix)

transformed_matrix.to_csv("combinedFramebinarized.csv", index=False)

print("Finished")
