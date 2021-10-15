import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
import numpy as np
import pandas as pd
import sklearn
from sklearn import preprocessing as pp
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import tensorflow.lite as tflite

number_of_gestures = 7
gestures = { '0': 'Clench-Fist', 
'1': 'Spider-Man',
'2': 'Thumb-to-pinky',
'3': 'Wrist-side-to-side-horizontal',
'4': 'Wrist-up-and-down',
'5': 'Wrist-rotate-inwards',
'6': 'Wrist-side-to-side-vertical',
'7': 'Pointer-finger'}

p = pd.read_excel('clean_data_mark.xlsx')

X = np.array(p.drop(['Classes'], axis=1))
Y = np.array(p['Classes'])
train_labels, train_samples = shuffle(X,Y)

scaler = pp.MinMaxScaler(feature_range=(0, 1))
scaled_train_samples = scaler.fit_transform(train_samples.reshape(-1,1))

model = Sequential([
    Dense(units=18, activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=number_of_gestures, activation='softmax')
])

X = np.asarray(X).astype('float32')
model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy']) 
# if you want to save the model fit the data using the save best model function and get rid of this line
model.fit(X, Y, epochs=30, shuffle=True, batch_size=30, use_multiprocessing=True, verbose=2)
'''
def save_best_model(x_data, y_data, repeats=15):
    best = (0, None)
    for n in range(repeats):
        x_train, x_test, y_train, y_test = train_test_split(x_data, y_data)
        model.fit(x_train, y_train, epochs=30, shuffle=True, batch_size=30, use_multiprocessing=True)
        acc = model.evaluate(x_data, y_data, use_multiprocessing=True)[1]
        if acc > best[0]:
            best = (acc, model)
    print(f'Best was {best[0] * 100}%')
    best[1].save('model.tf')
    lite_model = tflite.TFLiteConverter.from_keras_model(best[1])
    open("model.tflite", "wb").write(lite_model.convert())

save_best_model(X, Y)
'''