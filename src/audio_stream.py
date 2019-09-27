import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import struct
import time
import logging
import sys

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s][%(asctime)s] %(message)s')


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

        #logging the configured info
        logging.info({'CHUNK': self.CHUNK, 'RATE': self.RATE})

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
        try:

            # x variables for plotting
            x = np.arange(0, 2 * self.CHUNK, 2)
            xf = np.linspace(0, self.RATE, self.CHUNK)

            # create matplotlib figure and axes
            self.fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))
            self.fig.canvas.mpl_connect('button_press_event', self.onClick)

            # create a line object with random data
            self.line, = ax1.plot(x, np.random.rand(self.CHUNK), '-', lw=2)

            # create semilogx line for spectrum
            self.line_fft, = ax2.semilogx(xf,
                                          np.random.rand(self.CHUNK),
                                          '-',
                                          lw=2)

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
        except:
            logging.error('not possible to create plot')
            sys.exit(1)

    def start_plot(self):

        self.frame_count = 0
        self.start_time = time.time()

        data = self.stream.read(self.CHUNK)
        data_int = struct.unpack(str(2 * self.CHUNK) + 'B', data)
        data_np = np.array(data_int, dtype='b')[::2] + 128

        self.line.set_ydata(data_np)

        # compute FFT and update line
        yf = np.fft.fft(data_int)
        self.line_fft.set_ydata(np.abs(yf[0:self.CHUNK]) / (128 * self.CHUNK))

        # update figure canvas
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        self.frame_count += 1

    def exit_app(self):
        self.p.close(self.stream)

    def onClick(self, event):
        self.pause = True
