import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras import layers, models
import tensorflow as tf
import matplotlib.pyplot as plt
import glob
import cv2 as cv

from google.colab import drive
drive.mount('/content/drive')

def loadData(dataset):
    images = []
    labels = []
    for item in glob.glob(dataset):
      img = cv.imread(item)
      img = cv.resize(img, (32, 32))  # conforming images
      img = img / 255.0  # normalization
      images.append(img)
      label = item.split("/")[-2]
      labels.append(label)

    images = np.array(images)
    lb = LabelBinarizer()
    labels = lb.fit_transform(labels)
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=90)
    return X_train, X_test, y_train, y_test

def cnnModel():
    cnnModel = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', padding='same',
                      input_shape=(32,32,3)),
        layers.MaxPooling2D((2,2)),
        layers.Conv2D(64, (3,3), activation='relu', padding='same'),
        layers.MaxPooling2D((2,2)),
        layers.Flatten(),
        layers.Dense(32, activation='relu'),
        layers.Dense(11, activation='softmax')
    ])
    cnnModel.compile(loss='categorical_crossentropy', optimizer='sgd',
                     metrics=['accuracy'])
    return cnnModel


path = "/content/drive/MyDrive/Colab Notebooks/tamrin1_DL/dataset"
X_train, X_test, y_train, y_test = loadData(f'{path}/*/*')

cnn = cnnModel()
final_model = cnn.fit(x=X_train, y=y_train, batch_size=32, epochs=50, validation_data=(X_test, y_test))
cnn.save("finalModel.keras")