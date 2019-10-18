import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import struct


class Graphic(object):
    def __init__(self, chunk=1024, rate=44100):

        #CHUNK is the number of samples per frame
        self.CHUNK = chunk

        #RATE is the frequency of the samples
        self.RATE = rate

        #Exit the program using this flag
        self.pause = False

    def init_plots(self):

        #vectors for plotting
        self.freq_vect = self.RATE*np.arange(self.CHUNK//2)/self.CHUNK
        self.time_vect = np.arange(self.CHUNK, dtype=np.float32) / self.RATE * 1000

        #create matplotlib figure and axes
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, figsize=(15, 7))
        self.fig.canvas.mpl_connect('button_press_event', self.onClick)

        # format waveform axes
        self.ax1.set_title('AUDIO WAVEFORM')

        #setup the subplot of wave plot
        #self.ax1.set_ylim(-32768, 32768)
        self.ax1.set_ylim(-10000, 10000)
        self.ax1.set_xlim(0, self.time_vect.max())
        self.ax1.set_xlabel(u'time (ms)', fontsize=10)
        self.ax1.set_ylabel(u'Magnitude', fontsize=10)

        #setup the subplot of frequency plot
        #self.ax2.set_xscale('log')
        self.ax2.set_ylim(0, 4000)
        self.ax2.set_xlim(0, self.freq_vect.max())
        self.ax2.set_xlabel(u'frequency (Hz)', fontsize=10)
        self.ax2.set_ylabel(u'|Amplitude|', fontsize=10)

        #line objects
        self.line1, = self.ax1.plot(self.time_vect, np.ones_like(self.time_vect))
        self.line2, = self.ax2.plot(self.freq_vect, np.ones_like(self.freq_vect))

        #show axes
        thismanager = plt.get_current_fig_manager()
        thismanager.window.setGeometry(5, 120, 1910, 1070)
        plt.show(block=False)

    def plot(self, data, data_fft):

        #update wave plot
        self.line1.set_data(self.time_vect, data)

        #normalize data from fft
        #data_fft_max = np.abs(data_fft).max()
        # print('data')
        # print(data.max())

        # print('fft')
        # print(data_fft_max)
        # if (data_fft_max > 0):
        #     data_fft = [i / data_fft_max for i in data_fft]

        #update frequency plot
        #print(np.abs(data_fft))

        self.line2.set_data(self.freq_vect, ((np.abs(data_fft[:self.CHUNK//2])*2)/self.CHUNK))

        # update figure canvas
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def onClick(self, event):
        self.pause = True
