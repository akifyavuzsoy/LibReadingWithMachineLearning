
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv3D, LSTM, Dense, Dropout, Bidirectional, MaxPool3D, Activation, Reshape, SpatialDropout3D, BatchNormalization, TimeDistributed, Flatten

def load_model() -> Sequential:

    model = Sequential()
    model.add(Conv3D(128, 3, input_shape=(75, 46, 140, 1), padding='same'))
