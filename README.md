# Audio Analysis

A python project that uses audio stream from a microphone to analyze and plotting.

## Stream

The audio is capture from the microphone using a python package [PyAudio](https://pypi.org/project/PyAudio/). PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. 

Also, create a plotting figure using [matplotlib](https://matplotlib.org/).

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms

The plotting figure show the audio that is being captured and the spectrum.

The spectrum analysis was possible by implementing a algorithm that calculates  Fast Furrier Transform (FFT).  

## Fast Furrier Transform


The discrete Fourier transform (DFT) is a mathematical technique used to convert temporal or spatial data into frequency domain data. The DFT, is defined as:

<p align="center"><img src="/etc/images/b20654e3152b7d6cbc788a0bafeb6dea.svg?invert_in_darkmode&sanitize=true" align=middle width=203.45375819999998pt height=47.60747145pt/></p>
The FFT is a fast algorithm to compute the DFT. It's possible to divide the DFT computation into two smaller parts. From the definition of the DFT we have:
<p align="center"><img src="/etc/images/1090afb9ddf7d3e7ff1711af98a25e6b.svg?invert_in_darkmode&sanitize=true" align=middle width=585.9109476pt height=166.91377889999998pt/></p>

Based on the conclusion above, we design a algorithm to compute the FFT.


## Developing

#### Requirements

Dependencies on [Ubuntu](https://ubuntu.com/):
```bash
sudo apt-get install python3 \
                        python3-dev \
                        build-essential \
                        libssl-dev \
                        libffi-dev \
                        libxml2-dev \
                        libxslt1-dev \
                        zlib1g-dev\
                        libasound-dev \
                        portaudio19-dev \
                        libportaudio2 \
                        libportaudiocpp0

``` 
To install the requirements modules, just run:
```bash
pip3 install -r requirements.txt
``` 


