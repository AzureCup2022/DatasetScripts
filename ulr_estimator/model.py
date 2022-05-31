import tensorflow as tf
from tensorflow.keras import layers, models
import lzma
import os
import pickle

class ulr_model:

    def __init__(self):
        self.model = models.Sequential()
        self.model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(700, 700, 3)))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(64, activation='relu'))
        self.model.add(layers.Dense(2, activation='softmax'))

        self.model.summary()

        self.model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


    def train(self, X_imgs, X_labels, Y_imgs, Y_labels, epochs=100):
        self.history = self.model.fit(X_imgs, X_labels, epochs=epochs, 
                            validation_data=(Y_imgs, Y_labels))

    def predict(self, X_imgs):
        return self.model.predict(X_imgs)

    def save(self, model_path="./model.ulr"):
        # Save this model.
        with lzma.open(model_path, "wb") as model_file:
            pickle.dump(self, model_file)

    @staticmethod
    def load(model_path="./model.ulr"):
        # Load this model
        with lzma.open(model_path, "rb") as model_file:
            model = pickle.load(model_file)
        return model