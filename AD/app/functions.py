from PIL import Image
import numpy as np
from .predict import model
from django.conf import settings
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing import sequence
import pickle


history = []

def handle_question(text):
    pickleFile = open(settings.TOKENIZER, 'rb')
    tok = pickle.load(pickleFile)
    sentence = tok.texts_to_sequences([text])
    sentence = sequence.pad_sequences(sentence, maxlen = 150)

    result = model.predict(sentence)

    if result[0][0] > 0.5:
        result = 'You are rude'
    else:
        result = 'You are nice'
    
    history.append(text)
    history.append(result)

    # img.show()
    return history

