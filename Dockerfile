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
    libatlas-dev \
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

WORKDIR /mediagrabber

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt


COPY . /mediagrabber
RUN pip install -e .

ENV LOG_LEVEL=WARNING
ENV WORKDIR=/tmp
ENV AMQP_URL=amqp://guest:guest@host.docker.internal:5672/%2F
ENV AMQP_IN=mediagrabber.in
ENV AMQP_OUT=mediagrabber.out


ENV PYTHONUNBUFFERED=1

CMD ["python", "mediagrabber/amqp.py"]
