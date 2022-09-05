import os
import caer
import canaro
import numpy as np
import cv2
import gc
import matplotlib.pyplot as plt
from keras.callbacks import LearningRateScheduler
from keras.utils import to_categorical

IMG_SIZE = (60,60)
channels = 1
charPath = r'Simpsons Dataset/simpsons_dataset'

charDict = {}
for char in os.listdir(charPath):
    charDict[char] = len(os.listdir(os.path.join(charPath, char)))

#sorting
charDict = caer.sort_dict(charDict, descending=True)

characters = []
count = 0
for i in charDict:
    characters.append(i[0])
    count += 1
    if count >= 10:
        break

#Create training data
train = caer.preprocess_from_dir(charPath, characters, channels=channels, IMG_SIZE=IMG_SIZE, isShuffle=True)

featureSet, labels = caer.sep_train(train, IMG_SIZE=IMG_SIZE)
featureSet = caer.normalize(featureSet)
labels = to_categorical(labels, len(characters))

x_train, x_val, y_train, y_val = caer.train_val_split(featureSet, labels, val_ratio=2)

BATCH_SIZE = 32
EPOCHS = 20

#Image data generator
dataGen = canaro.generators.imageDataGenerator()
train_gen = dataGen.flow(x_val, y_val, batch_size=BATCH_SIZE)

model = canaro.models.createSimpsonsModel(IMG_SIZE=IMG_SIZE, channels=channels, output_dim=len(characters), loss='binary_crossentropy', decay=1e-6, 
learning_rate=0.001, momentum=0.9, nesterov=True)

callbacks_list = [LearningRateScheduler(canaro.lr_schedule)]

training = model.compile(train_gen, steps_per_epoch=len(x_train)//BATCH_SIZE, 
                    epochs=EPOCHS,
                    validation_data=(x_val, y_val),
                    validation_steps=len(y_val)//BATCH_SIZE,
                    callbacks = callbacks_list)