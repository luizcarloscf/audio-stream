## Fast Furrier Transform

Implementation of a Fast Fourier Transform (FFT) in Python. 

### About 

The discrete Fourier transform (DFT) is a mathematical technique used to convert temporal or spatial data into frequency domain data. The DFT, is defined as:

<p align="center"><img src="/tex/b20654e3152b7d6cbc788a0bafeb6dea.svg?invert_in_darkmode&sanitize=true" align=middle width=203.45375819999998pt height=47.60747145pt/></p>
The FFT is a fast algorithm to compute the DFT. It's possible to divide the DFT computation into two smaller parts. From the definition of the DFT we have:
<p align="center"><img src="/tex/1090afb9ddf7d3e7ff1711af98a25e6b.svg?invert_in_darkmode&sanitize=true" align=middle width=585.9109476pt height=166.91377889999998pt/></p>

Based on the conclusion above, we design a algorithm to compute the FFT.


### Developing

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


