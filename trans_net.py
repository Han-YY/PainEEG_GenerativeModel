## The networks in different steps of the adversarial model
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import layers

# The neural network for clasifying the labels with the connectivity features
def classifier_model():
    dim = (32, 32, 1)
    input_shape = (dim)
    Input_words = layers.Input(shape=input_shape, name='inpud_vid')
    # CNN
    x = layers.Conv2D(filters=128, kernel_size=(7,7), padding='same', activation='relu')(Input_words)
    x = layers.MaxPooling2D(pool_size=(3,3))(x)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(filters=64, kernel_size=(5,5), padding='same', activation='relu')(Input_words)
    x = layers.MaxPooling2D(pool_size=(3,3))(x)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(filters=32, kernel_size=(3,3), padding='same', activation='relu')(Input_words)
    x = layers.MaxPooling2D(pool_size=(3,3))(x)
    x = layers.BatchNormalization()(x)
    x = layers.SpatialDropout2D(0.2)(x)
    # Flatten
    x = layers.Flatten()(x)
    x = layers.Dense(100, kernel_regularizer='l2')(x)
    x = layers.Activation('relu')(x)
    x = layers.Flatten()(x)
    x = layers.Activation('sigmoid')(x)
    x = layers.Dense(2)(x)
    out = layers.Softmax()(x)
    model = keras.Model(inputs=Input_words, outputs=[out])

    return model

def adversary_model():
    dim = (32, 32, 1)
    input_shape = (dim)
    Input_words = layers.Input(shape=input_shape, name='inpud_vid')
    # CNN
    x = layers.Conv2D(filters=16, kernel_size=(3,3), padding='same', activation='relu')(Input_words)
    x = layers.BatchNormalization()(x)
    x = layers.Flatten()(x)
    x = layers.Dense(36)(x)
    out = layers.Softmax()(x)
    model = keras.Model(inputs=Input_words, outputs=[out])

    return model
