from audio_stream import AudioStream
from utils import error_messages
from fft import Fft
from recorder import MicrophoneRecorder
import logging
import time

logging.basicConfig(level=logging.INFO, format='[%(levelname)s][%(asctime)s] %(message)s')

if __name__ == '__main__':

    #hadling with error messages from ALSA
    error_messages()

    mic = MicrophoneRecorder(44100, 1024)

    #Furrier Transform Object
    fft = Fft(1024, True)

    #object for stream
    audio = AudioStream(rate=44100, chunk=1024)

    #logging configurations
    logging.info({'CHUNK': audio.CHUNK, 'RATE': audio.RATE})

    #initialize our figure
    audio.init_plots()

    #variables to measurement performance
    frames = 0
    start_time = time.time()

    #start capture audio and plotting
    while audio.pause is not True:

        data = mic.get_frames()
        if len(data) > 0:
            audio.plot(data=data[-1], data_fft=fft.transform(data[-1]))
            frames += 1

    #info of perfomance
    logging.info({'fps': round(frames / (time.time() - start_time), 2)})

    #exiting
    mic.close()