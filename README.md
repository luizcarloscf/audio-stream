# Audio Stream
Audio is capture from the microphone and plotting the wave form in time and frequency domain.
## Usage
Run on terminal:
```bash
git clone https://github.com/luizcarloscf/audio-stream.git
cd audio-stream
./bootstrap.sh
python3 src/main.py
```
For more informations about what can be configurated just run:
```bash
python3 src/main.py --help
```

## About

### Audio recorder
The audio is capture from the microphone using a python package [PyAudio](https://pypi.org/project/PyAudio/) on a thread. PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. 

### Fast Fourier Transform
The audio analysis to get the data on frequency domain is compute by the Fast Fourier Transform.


The discrete Fourier transform (DFT) is a mathematical technique used to convert temporal or spatial data into frequency domain data. The DFT, is defined as:

<p align="center"><img src="/etc/images/b20654e3152b7d6cbc788a0bafeb6dea.svg?invert_in_darkmode&sanitize=true" align=middle width=203.45375819999998pt height=47.60747145pt/></p>
The FFT is a fast algorithm to compute the DFT. It's possible to divide the DFT computation into two smaller parts. From the definition of the DFT we have:
<p align="center"><img src="/etc/images/1090afb9ddf7d3e7ff1711af98a25e6b.svg?invert_in_darkmode&sanitize=true" align=middle width=585.9109476pt height=166.91377889999998pt/></p>

Based on the conclusion above, we design a algorithm to compute the FFT.

### Graphic

Create a plotting figure using [matplotlib](https://matplotlib.org/).

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms

The plotting figure show the audio that is being captured and the spectrum.

## Developing

### Requirements

To install the dependencies on [Ubuntu](https://ubuntu.com/), just run:
```bash
./bootstrap.sh
``` 








