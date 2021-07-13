FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && \
    apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3 \
    python3-pip \
    python3-dev \
    python3-numpy \
    software-properties-common \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    wget \
    aria2 \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN which python3
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY install-packages.sh .
RUN chmod +x ./install-packages.sh
RUN ./install-packages.sh

# Testing tools
RUN pip install flake8 pytest pytest-cov

COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY test.py .
RUN python test.py
