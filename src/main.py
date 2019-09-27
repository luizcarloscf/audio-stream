import logging
import time
from audio_stream import AudioStream
from utils import error_messages

if __name__ == '__main__':

    #hadling with error messages from ALSA
    error_messages()

    #object for stream
    audio = AudioStream(rate=44100, chunk=1024)

    #initialize our figure
    audio.init_plots()

    #ploting
    while audio.pause is False:
        audio.start_plot()

    #info
    logging.info({'FPS': audio.frame_count / (time.time() - audio.start_time)})

    #exiting
    audio.exit_app()