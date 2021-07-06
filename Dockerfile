FROM python:3.8

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
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

COPY install-packages.sh .
RUN chmod +x ./install-packages.sh
RUN ./install-packages.sh

COPY aria2c /usr/bin/aria2c
RUN chmod +x /usr/bin/aria2c
RUN echo "Aria2c version:" && /usr/bin/aria2c --version

# Testing tools
RUN pip install flake8 pytest pytest-cov

COPY requirements.txt .
RUN pip install -r ./requirements.txt
