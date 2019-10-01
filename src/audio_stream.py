import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import struct


class AudioStream(object):
    def __init__(self, chunk=2048, rate=44100):

        #CHUNK is the number of samples per frame
        self.CHUNK = chunk

        #RATE is the frequency of the samples
        self.RATE = rate

        #other configurations
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.pause = False

        #stream object
        self.p = pyaudio.PyAudio()

        #open the stream
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK,
        )

    def init_plots(self):

        # x variables for plotting
        x = np.arange(0, 2 * self.CHUNK, 2)
        xf = np.linspace(0, self.RATE, self.CHUNK)

        # create matplotlib figure and axes
        self.fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))
        self.fig.canvas.mpl_connect('button_press_event', self.onClick)

        # create a line object with random data
        self.line, = ax1.plot(x, np.random.rand(self.CHUNK), '-', lw=2)

        # create semilogx line for spectrum
        self.line_fft, = ax2.semilogx(xf, np.random.rand(self.CHUNK), '-', lw=2)

        # format waveform axes
        ax1.set_title('AUDIO WAVEFORM')
        ax1.set_xlabel('samples')
        ax1.set_ylabel('volume')
        ax1.set_ylim(0, 255)
        ax1.set_xlim(0, 2 * self.CHUNK)
        plt.setp(
            ax1,
            yticks=[0, 128, 255],
            xticks=[0, self.CHUNK, 2 * self.CHUNK],
        )
        plt.setp(
            ax2,
            yticks=[0, 1],
        )

        # format spectrum axes
        ax2.set_xlim(20, self.RATE / 2)

        # show axes
        thismanager = plt.get_current_fig_manager()
        thismanager.window.setGeometry(5, 120, 1910, 1070)
        plt.show(block=False)

    def get_data(self):

        data = self.stream.read(self.CHUNK, exception_on_overflow=False)
        data_int = struct.unpack(str(2 * self.CHUNK) + 'B', data)
        return data_int

    def plot(self, data, data_fft):

        self.line.set_ydata(np.array(data, dtype='b')[::2] + 128)
        self.line_fft.set_ydata(np.abs(data_fft[0:self.CHUNK]) / (128 * self.CHUNK))

        # update figure canvas
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def exit_app(self):
        self.p.close(self.stream)

    def onClick(self, event):
        self.pause = True
