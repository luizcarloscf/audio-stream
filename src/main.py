import logging
import time
from audio_stream import AudioStream
from utils import error_messages
from fft import Fft

if __name__ == '__main__':

    #hadling with error messages from ALSA
    error_messages()

    #Furrier Transform Object
    fft = Fft()

    fft.start(2048, True)

    #object for stream
    audio = AudioStream(rate=44100, chunk=1024)

    #initialize our figure
    audio.init_plots()

    #variables to measurement performance
    start_time = time.time()
    frames = 0

    #start capture audio and plotting
    while audio.pause is not True:

        #getting data from the buffer
        data = audio.get_data()
        audio.plot(data=data, data_fft=fft.transform(data))
        frames += 1

    #infos of perfomance
    logging.info({'fps': round(frames / (time.time() - start_time), 2)})

    #exiting
    audio.exit_app()