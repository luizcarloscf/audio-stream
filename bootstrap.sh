#!/bin/bash

if [[ $EUID != 0 ]]; then
  export wasnt_root=true
  sudo -E "$0" "$@"
fi

if [[ $EUID == 0 ]]; then

  packages=(build-essential \
            sudo \
            python3 \
            python3-dev \
            libssl-dev \
            libffi-dev \
            libxml2-dev \
            libxslt1-dev \
            zlib1g-dev \
            libasound-dev \
            portaudio19-dev \
            libportaudio2 \
            libportaudiocpp0)

    echo "[$EUID] |>>| installing distro packages: ${packages[*]}"
    apt update
    apt install --no-install-recommends -y ${packages[*]} 


  if ! command -v pip3 > /dev/null; then 
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py
    rm -f get-pip.py
  fi
fi

if [[ $EUID != 0 || -z ${wasnt_root} ]]; then
    pip3 install --user -r requirements.txt
fi