import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import struct


class Graphic(object):
    def __init__(self, chunk=1024, rate=44100, scale=32678, norm=False):

        #scale of the graphic
        self.scale = int(scale)

        #normalization
        self.norm = norm

        #CHUNK is the number of samples per frame
        self.CHUNK = chunk

        #RATE is the frequency of the samples
        self.RATE = rate

        #Exit the program using this flag
        self.pause = False

    def init_plots(self):

        #vectors for plotting
        self.freq_vect = self.RATE * np.arange(self.CHUNK // 2) / self.CHUNK
        self.time_vect = np.arange(self.CHUNK, dtype=np.float32) / self.RATE * 1000

        #create matplotlib figure and axes
        self.fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))
        self.fig.canvas.mpl_connect('button_press_event', self.onClick)

        # format waveform axes
        ax1.set_title('AUDIO WAVEFORM')

        #setup the subplot of wave plot
        ax1.set_ylim(-self.scale, self.scale)
        ax1.set_xlim(0, self.time_vect.max())
        ax1.set_xlabel(u'time (ms)', fontsize=10)
        ax1.set_ylabel(u'Magnitude', fontsize=10)

        #setup the subplot of frequency plot
        if self.norm == True:
            ax2.set_ylim(0, 1)
        else:
            ax2.set_ylim(0, self.scale)
        ax2.set_xlim(0, self.freq_vect.max())
        ax2.set_xlabel(u'frequency (Hz)', fontsize=10)
        ax2.set_ylabel(u'|Amplitude|', fontsize=10)

        #line objects
        self.line1, = ax1.plot(self.time_vect, np.ones_like(self.time_vect))
        self.line2, = ax2.plot(self.freq_vect, np.ones_like(self.freq_vect))

        #show axes
        thismanager = plt.get_current_fig_manager()
        thismanager.window.setGeometry(5, 120, 1910, 1070)
        plt.show(block=False)

    def plot(self, data, data_fft):

        #update wave plot
        self.line1.set_data(self.time_vect, data)

        #normalize data from fft
        if self.norm == True:
            data_fft = [i / self.scale for i in data_fft]

        #update frequency plot
        self.line2.set_data(self.freq_vect, ((np.abs(data_fft[:self.CHUNK // 2]) * 2) / self.CHUNK))

        # update figure canvas
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def onClick(self, event):
        self.pause = True
