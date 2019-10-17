from recorder import MicrophoneRecorder
from audio_stream import Graphic
from utils import error_messages
from fft import Fft

import logging
import time

logging.basicConfig(level=logging.INFO, format='[%(levelname)s][%(asctime)s] %(message)s')

if __name__ == '__main__':

    #hadling with error messages from ALSA
    error_messages()

    #object for capture the audio
    mic = MicrophoneRecorder(44100, 1024)

    #Furrier Transform Object
    fft = Fft(1024, True)

    #object for stream with matplotlib
    graphic = Graphic(rate=44100, chunk=1024)

    #logging configurations
    logging.info({'CHUNK': graphic.CHUNK, 'RATE': graphic.RATE})

    #initialize our figure
    graphic.init_plots()

    #variables to measurement performance
    frames = 0
    start_time = time.time()

    #start capture audio and plotting
    while graphic.pause is not True:

        #get all buffer of audio
        data = mic.get_frames()

        if len(data) > 0:

            #plotting only the last frame of audio captured
            graphic.plot(data=data[-1], data_fft=fft.transform(data[-1]))

        frames += 1

    #info of perfomance
    logging.info({'fps': round(frames / (time.time() - start_time), 2)})

    #exiting
    mic.close()