import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import struct


class AudioStream(object):
    def __init__(self, chunk=1024, rate=44100):

        #CHUNK is the number of samples per frame
        self.CHUNK = chunk

        #RATE is the frequency of the samples
        self.RATE = rate
        self.pause = False

    def init_plots(self):

        self.freq_vect = np.fft.fftfreq(self.CHUNK, 1. / self.RATE)
        self.time_vect = np.arange(self.CHUNK, dtype=np.float32) / self.RATE * 1000

        # create matplotlib figure and axes
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, figsize=(15, 7))
        self.fig.canvas.mpl_connect('button_press_event', self.onClick)

        self.ax1.set_ylim(-32768, 32768)
        self.ax1.set_xlim(0, self.time_vect.max())
        self.ax1.set_xlabel(u'time (ms)', fontsize=10)
        self.ax1.set_ylabel(u'Magnitude', fontsize=10)

        self.ax2.set_ylim(0, 1)
        self.ax2.set_xlim(0, self.freq_vect.max())
        self.ax2.set_xlabel(u'frequency (Hz)', fontsize=10)
        self.ax2.set_ylabel(u'|Amplitude|', fontsize=10)
        # line objects
        self.line1, = self.ax1.plot(self.time_vect, np.ones_like(self.time_vect))

        self.line2, = self.ax2.plot(self.freq_vect, np.ones_like(self.freq_vect))

        # format waveform axes
        self.ax1.set_title('AUDIO WAVEFORM')

        # show axes
        thismanager = plt.get_current_fig_manager()
        thismanager.window.setGeometry(5, 120, 1910, 1070)
        plt.show(block=False)

    def plot(self, data, data_fft):

        self.line1.set_data(self.time_vect, data)

        #normalize
        data_fft_max = np.abs(data_fft).max()

        if (data_fft_max > 0):
            data_fft = [i / data_fft_max for i in data_fft]

        print(len(data))
        print(len(data_fft))
        print(len(self.freq_vect))

        self.line2.set_data(self.freq_vect, np.abs(data_fft))

        # update figure canvas
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def onClick(self, event):
        self.pause = True
