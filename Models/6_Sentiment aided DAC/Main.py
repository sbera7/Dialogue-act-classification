
#Libraries
import re
import numpy as np
import pandas as pd
from matplotlib.pyplot import *
import keras
from keras.models import load_model
from keras.layers import *
from keras.preprocessing.text import Tokenizer 
from keras.preprocessing.sequence import pad_sequences
from keras.layers import *
from keras import backend as K
from keras import layers


import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"
df = pd.read_csv("C:\\Users\\user1\\Desktop\\required\\test_SA.csv")
def processed_data(data):
    data=data.drop(columns=["Unnamed: 0"])
    data['Utterances'] = data['Utterances'].apply(lambda x: x.lower())
    data['Utterances'] = data['Utterances'].apply(lambda x: re.sub('[^a-zA-z0-9\s]','',x))

    y = pd.get_dummies(data['Basic']).values

    return data,y



full_data = pd.read_csv('C:\\Users\\user1\\Desktop\\required\\full_SA.csv')
MAX_PADDING = 99
def x_value(data):
    tokenizer = Tokenizer(num_words = 16000, split=" ")
    tokenizer.fit_on_texts(full_data['Utterances'].values)
    x = tokenizer.texts_to_sequences(data['Utterances'].values)
    x = pad_sequences(x, padding='post', maxlen=MAX_PADDING)

    return x

train_data = pd.read_csv('C:\\Users\\user1\\Desktop\\required\\train_SA.csv')
train_data,y_train = processed_data(train_data)
x_train = x_value(train_data)
train_sen = np.array(train_data['SA'])
train_sen = train_sen.reshape(75066, 1)
x_train = np.concatenate((x_train, train_sen), axis=1)



val_data = pd.read_csv('C:\\Users\\user1\\Desktop\\required\\val_SA.csv')
val_data,y_val = processed_data(val_data)
x_val = x_value(val_data)
val_sen = np.array(val_data['SA'])
val_sen = val_sen.reshape(16432, 1)
x_val = np.concatenate((x_val, val_sen), axis=1)

test_data = pd.read_csv('C:\\Users\\user1\\Desktop\\required\\test_SA.csv')
test_data,y_test = processed_data(test_data)
x_test = x_value(test_data)
test_sen = np.array(test_data['SA'])
test_sen = test_sen.reshape(16701, 1)
x_test = np.concatenate((x_test, test_sen), axis=1)

MAX_LENGTH_PER_SENTENCE=100
units = 128
drop = 0.2
encoder_input = keras.Input(shape=(MAX_LENGTH_PER_SENTENCE))

def module(encoder_input):
    x =layers.Embedding(input_dim=16000, 
                        output_dim=256, 
                        input_length=x_train.shape[1])(encoder_input)
                                
    activations = Bidirectional(LSTM(units, 
                                    dropout=0.3, 
                                    recurrent_dropout=0.2,
                                    return_sequences=True))(x)

    attention = Dense(1, activation='tanh')(activations)
    attention = Flatten()(attention)
    attention = Activation('softmax')(attention)
    attention = RepeatVector(units*2)(attention)
    attention = Permute((2, 1))(attention)

    sent_representation = Multiply()([activations, attention])
    sent_representation = Lambda(lambda xin: K.sum(xin, axis=-2), 
                                output_shape=(units*2,))(sent_representation)

    reshape = Reshape((-1, 1, 256))(sent_representation)
    flat = TimeDistributed(Flatten())(reshape)
    dense_1 = Dense(5, activation='relu')(flat)
    dropout_1 = Dropout(drop)(dense_1)


    #conversation level
    biLSTM1 = Bidirectional(LSTM(5, return_sequences='true'))(dropout_1)
    biLSTM2 = Bidirectional(LSTM(5))(biLSTM1)

    dense_2 = Dense(5, activation='relu')(biLSTM2)
    dropout_2 = Dropout(drop)(dense_2)


    dropout_flat = Flatten()(dropout_1)
    merged_2 = concatenate([dropout_flat, dropout_2])
    dense_3 = Dense(units=5, input_shape=(1,))(merged_2)
    output = Activation('softmax')(dense_3)

    return output


model = keras.Model(inputs=[encoder_input], outputs=[module(encoder_input)])
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.summary()

early_stopping = keras.callbacks.EarlyStopping(monitor='accuracy', 
                                               mode='auto', 
                                               patience=1, 
                                               verbose=1)

'''model.fit(x_train, y_train, 
          epochs=100, 
          batch_size=32, 
          verbose=1,
          callbacks=[early_stopping],
          validation_data=(x_val, y_val))'''


model.save('SAVED_MODEL.h5')

saved_model = load_model('SAVED_MODEL.h5')

saved_model.evaluate(x_test,y_test)

y_pred = saved_model.predict(x_test)

y_pred = np.argmax(y_pred, axis=1)
y_test = np.argmax(y_test, axis=1)


from sklearn.metrics import confusion_matrix
confusion = confusion_matrix(y_test, y_pred)
print('Confusion Matrix\n')
print(confusion)


import matplotlib.pyplot as plt
import seaborn as sns

ax = sns.heatmap(confusion, annot=True, cmap='Blues')

ax.set_title('Confusion Matrix\n\n')
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ')

ax.xaxis.set_ticklabels(['B','D','F','Q','S'])
ax.yaxis.set_ticklabels(['B','D','F','Q','S'])

## Display the visualization of the Confusion Matrix.
plt.show()

from sklearn.metrics import f1_score
print("F1 score(macro)",f1_score(y_test, y_pred, average='macro'))
print("F1 score(micro)",f1_score(y_test, y_pred, average='micro'))