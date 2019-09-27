import numpy as np


class Fft(object):
    def __init__(self):
        pass

    def transform(self, data):
        return list(np.fft.fft(data))