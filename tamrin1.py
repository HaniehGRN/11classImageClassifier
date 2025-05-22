import numpy as np
import cv2 as cv
from keras import models
import sys

class Predictor():
    def __init__(self):
        self.classes = {0: '206', 1: 'bird', 2:'carpet', 3: 'cat', 4: 'cellphone', 5: 'dog',
                   6: 'fish', 7: 'horse', 8: 'laptop', 9: 'perfume', 10: 'sheep'}
        self.cnnModel = models.load_model("models/finalModel.keras")
    def predict(self, img):
        self.img = cv.imread(img)
        self.n_img = cv.resize(self.img, (32, 32))  # Resize to the input shape expected by the model
        self.n_img = self.n_img / 255.0  # Normalize pixel values to [0, 1]
        self.n_img = self.n_img.reshape(1, 32, 32, 3)
        self.predictions = self.cnnModel.predict(self.n_img)
        self.predicted_class = np.argmax(self.predictions)
        print(f"Predicted class: {self.classes[self.predicted_class]}")
        return self.classes[self.predicted_class]

# predictor = Predictor()
# predictor.predict("testImages/perfumetest.jpeg")

