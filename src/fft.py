import numpy as np


class Fft(object):
    def __init__(self, len_vector, inverse):

        self.n = len_vector
        self.levels = self.n.bit_length() - 1
        if 2**self.levels != self.n:
            raise ValueError("Length is not a power of 2")

        coef = (2 if inverse else -2) * np.pi / len_vector
        self.exptable = [np.exp(1j * i * coef) for i in range(len_vector // 2)]

    def transform_numpy(self, data):
        return list(np.fft.fft(data))

    def reversed_bit(self, data, bits):
        y = 0
        for i in range(bits):
            y = (y << 1) | (data & 1)
            data >>= 1
        return y

    def transform(self, vector):

        vector = [
            vector[self.reversed_bit(i, self.levels)] for i in range(self.n)
        ]

        size = 2
        while size <= self.n:
            halfsize = size // 2
            tablestep = self.n // size
            for i in range(0, self.n, size):
                k = 0
                for j in range(i, i + halfsize):
                    temp = vector[j + halfsize] * self.exptable[k]
                    vector[j + halfsize] = vector[j] - temp
                    vector[j] += temp
                    k += tablestep
            size *= 2
        return vector
