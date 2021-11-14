from textblob import TextBlob
y = "You are good"
edu = TextBlob(y)
x=edu.sentiment.polarity
print(x)

import numpy as np
import pandas as pd
SA = np.array([])
dataframe = pd.read_csv("C:\\Users\\user1\\Documents\\repo\\dialog act RNN\MRDA\\val.csv")
#print(dataframe)
#print(dataframe['Text'][4])
for i in range (16432):
    y = dataframe['Utterances'][i]
    edu = TextBlob(y)
    x = edu.sentiment.polarity
    if x>0:
        SA = np.append(SA, 13000)
    elif x<0:
        SA = np.append(SA, 14000)
    else:
        SA = np.append(SA, 15000)

print("hello")
print("hi")
dataframe.insert(2, "SA", SA, True)
print(dataframe)
dataframe.to_csv("C:\\Users\\user1\\Desktop\\val_SA.csv")
