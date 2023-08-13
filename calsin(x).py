# -*- coding: utf-8 -*-
"""calsin(x).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PO4alAE6FOBiN4lsCuiABpuCGZZxO34S
"""

import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense,Input
from sklearn.model_selection import train_test_split

x = np.linspace(-2*np.pi,2*np.pi,10000).reshape(-1,1)
y = np.sin(x)

XTrain, XVal, YTrain, YVal = train_test_split(x,y, test_size=0.2)



model=Sequential()
model.add(Dense(40,activation='sigmoid'))
model.add(Dense(12,activation='sigmoid'))
model.add(Dense(10,activation='sigmoid'))
model.add(Dense(12,activation='sigmoid'))
model.add(Dense(50,activation='sigmoid'))
model.add(Dense(1))

model.compile(loss='mean_squared_error' ,optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),metrics=['mean_squared_error'])

his = model.fit(XTrain,YTrain,epochs=200,batch_size=16,validation_data=(XVal,YVal))

model.summary()



model.predict([30*np.pi/180])

model.predict([-30*np.pi/180])

model.predict([45*np.pi/180])

model.predict([-45*np.pi/180])

model.predict([90*np.pi/180])

model.predict([-90*np.pi/180])

model.predict([50*np.pi/180])

model.predict([270*np.pi/180])

model.predict([-270*np.pi/180])

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot((his.history['loss']), label = " Training Loss ")
plt.plot((his.history['val_loss']), label = " Validation Loss ")
plt.legend()

















model.summary()

tf.keras.utils.plot_model(model,show_shapes=True)







import torch

x = torch.randn(10,3)
y = torch.randn(10,2)

fc = torch.nn.Linear(3,2)
print("w = ", fc.weight)
print("b = ", fc.bias)

loss_func = torch.nn.MSELoss()
optimizer = torch.optim.SGD(fc.parameters(), lr=0.01)

y_pred = fc(x)
print(y_pred)

loss_value = loss_func(y_pred, y)
print(loss_value.item())

loss_value.backward()
print(fc.weight.grad)
print(fc.bias.grad)

optimizer.step()
print(fc.weight)

