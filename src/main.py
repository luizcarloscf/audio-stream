from recorder import MicrophoneRecorder
from graphic import Graphic
from utils import error_messages
from fft import Fft
from fir import fir

import numpy as np
import argparse
import logging
import time


def main():

    parser = argparse.ArgumentParser(description='Audio Stream')

    parser.add_argument('-c',
                        '--chunk',
                        action='store',
                        dest='chunk',
                        default=1024,
                        required=False,
                        help='Number of samples')

    parser.add_argument('-r',
                        '--rate',
                        action='store',
                        dest='rate',
                        default=44100,
                        required=False,
                        help='Frenquecy of sampling')

    parser.add_argument('-n',
                        '--normalize',
                        action='store_true',
                        dest='norm',
                        help='Normalize graphic')

    parser.add_argument('-y',
                        '--y-scale',
                        action='store',
                        dest='y_scale',
                        default=32678,
                        help='Scale of data in Y at graphic')


    #getting the arguments
    args = parser.parse_args()

    #logging level
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s][%(asctime)s] %(message)s')

    #hadling with error messages from ALSA
    error_messages()

    #object for capture the audio
    mic = MicrophoneRecorder(chunksize=args.chunk, rate=args.rate)

    #Furrier Transform Object
    fft = Fft(len_vector=args.chunk, inverse=True)

    has_filter = True
    low_pass = False
    band_pass = True

    if low_pass:
        f1 = 9000 / args.rate
        f2 = 0
        filter_lp = fir(args.chunk, f1, f2, filter_type='low_pass')
    

    elif band_pass:
        f1 = 2500 / args.rate
        f2 = 9000 / args.rate
        filter_lp = fir(args.chunk, f1, f2, filter_type='band_pass')
    



    #object for stream with matplotlib
    graphic = Graphic(rate=args.rate, chunk=args.chunk, scale=args.y_scale, norm=args.norm)

    #logging configurationsself
    logging.info({'CHUNK': args.chunk, 'RATE': args.rate})

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

            if has_filter:
                signal = data[-1]
                signal_filtered_lp = np.zeros(len(signal))
                for i in range(len(data[-1])):
                    signal_filtered_lp[i] = filter_lp.filter(signal[i])

                #plotting only the last frame of audio captured
                graphic.plot(data=signal_filtered_lp, data_fft=fft.transform(signal_filtered_lp))
            
            else:

                #plotting only the last frame of audio captured
                graphic.plot(data=data[-1], data_fft=fft.transform(data[-1]))

    
        frames += 1

    #info of perfomance
    logging.info({'fps': round(frames / (time.time() - start_time), 2)})

    #exiting
    mic.close()


if __name__ == '__main__':
    main()
