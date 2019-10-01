## Fast Furrier Transform

Implementation of a Fast Fourier Transform (FFT) in Python. 

### About 

The discrete Fourier transform (DFT) is a mathematical technique used to convert temporal or spatial data into frequency domain data. The DFT, is defined as:

$$
\begin{aligned}
X_k = \sum_{n=0}^{N-1} x_n \cdot e^{-i~2\pi~k~n~/~N}
\end{aligned}
$$
The FFT is a fast algorithm to compute the DFT. It's possible to divide the DFT computation into two smaller parts. From the definition of the DFT we have:
$$
\begin{aligned}
X_k &= \sum_{n=0}^{N-1} x_n \cdot e^{-i~2\pi~k~n~/~N} \\
    &= \sum_{m=0}^{N/2 - 1} x_{2m} \cdot e^{-i~2\pi~k~(2m)~/~N} + \sum_{m=0}^{N/2 - 1} x_{2m + 1} \cdot e^{-i~2\pi~k~(2m + 1)~/~N} \\
    &= \sum_{m=0}^{N/2 - 1} x_{2m} \cdot e^{-i~2\pi~k~m~/~(N/2)} + e^{-i~2\pi~k~/~N} \sum_{m=0}^{N/2 - 1} x_{2m + 1} \cdot e^{-i~2\pi~k~m~/~(N/2)}
\end{aligned}
$$

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


