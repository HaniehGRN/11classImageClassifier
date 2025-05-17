import numpy as np
import cv2 as cv
from keras import models

classes = {0: '206', 1: 'bird', 2:'carpet', 3: 'cat', 4: 'cellphone', 5: 'dog',
           6: 'fish', 7: 'horse', 8: 'laptop', 9: 'perfume', 10: 'sheep'}
cnnModel = models.load_model("model/finalModel.keras")
image_path = 'cow.png'
img = cv.imread(image_path)  # Use IMREAD_COLOR if it's a color model
n_img = cv.resize(img, (32, 32))  # Resize to the input shape expected by the model
n_img = n_img / 255.0  # Normalize pixel values to [0, 1]
n_img = n_img.reshape(1, 32, 32, 3)  # Add batch and channel dimensions
predictions = cnnModel.predict(n_img)
predicted_class = np.argmax(predictions)
print(f"Predicted class: {classes[predicted_class]}")
cv.imshow("image.png", img)
cv.waitKey(0)
