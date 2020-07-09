import tensorflow as tf
from tensorflow.keras.layers import Layer, Conv2D, DepthwiseConv2D, BatchNormalization
from tensorflow.keras import datasets, models, layers
from tqdm import tqdm
import numpy as np
from tensorflow.keras.mixed_precision import experimental as mixed_precision
import os
import urllib
import tarfile
from pathlib import Path
import pickle
import pandas as pd

from keras.models import Model
from keras.layers import Dense, Embedding, Input, LSTM, Bidirectional, GlobalMaxPool1D, Dropout
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.callbacks import EarlyStopping, ModelCheckpoint

from django.conf import settings


with open(settings.JSON_FILE) as json_file:
    json_config = json_file.read()

model = models.model_from_json(json_config)
model.load_weights(settings.WEIGHTS)
