from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.optimizers import RMSprop

import urllib
import matplotlib.image  as mpimg
import matplotlib.pyplot as plt


def modelnet(weights_file):    # Instantiate the model
        pre_trained_model = InceptionV3(input_shape=(150, 150, 3),
                                        include_top=False,
                                        weights=None)

        # load pre-trained weights
        pre_trained_model.load_weights(weights_file)

        # freeze the layers
        for layer in pre_trained_model.layers:
            layer.trainable = False

        # pre_trained_model.summary()

        last_layer = pre_trained_model.get_layer('mixed7')
        print('last layer output shape: ', last_layer.output_shape)
        last_output = last_layer.output

        x = layers.Flatten()(last_output)

        x = layers.Dense(1024, activation='relu')(x)

        x = layers.Dense(1, activation='sigmoid')(x)

        model = Model(pre_trained_model.input, x)
        

        model.compile(optimizer=RMSprop(lr=0.0001),
                    loss='binary_crossentropy',
                    metrics=['acc'])
        return model
12