FROM debian:stretch

MAINTAINER Yuhang Wang <yuhangw@gmail.com>

# install debian packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get update -qq \
 && apt-get install --no-install-recommends -y \
    # install essentials
    build-essential \
    g++ \
    git \
    openssh-client \
    # install python 2
    python \
    python-dev \
    python-pip \
    python-setuptools \
    python-virtualenv \
    python-wheel \
    pkg-config \
    # requirements for numpy
    libopenblas-base \
    python-numpy \
    python-scipy \
    # requirements for keras
    python-h5py \
    python-yaml \
    python-pydot \
    uwsgi-plugin-python \
    nginx \
    supervisor \
    nano \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ARG TENSORFLOW_VERSION=1.3.0
ARG TENSORFLOW_DEVICE=cpu
ARG TENSORFLOW_APPEND=
RUN pip --no-cache-dir install https://storage.googleapis.com/tensorflow/linux/${TENSORFLOW_DEVICE}/tensorflow${TENSORFLOW_APPEND}-${TENSORFLOW_VERSION}-cp27-none-linux_x86_64.whl

ARG KERAS_VERSION=2.0.8
ENV KERAS_BACKEND=tensorflow
RUN pip --no-cache-dir install --no-dependencies git+https://github.com/fchollet/keras.git@${KERAS_VERSION}

# quick test and dump package lists
RUN python -c "import tensorflow; print(tensorflow.__version__)" \
 && dpkg-query -l > /dpkg-query-l.txt \
 && pip2 freeze > /pip2-freeze.txt

RUN apt-get update -qq \
 && apt-get install --no-install-recommends -y \
    python-matplotlib \
    python-pillow \
    sqlite3

# install additional python packages
RUN pip --no-cache-dir install \
    # jupyter notebook and ipython (Python 2)
    ipython \
    ipykernel \
    jupyter \
    # data analysis (Python 2)
    pandas \
    scikit-learn \
    statsmodels \
    seaborn \
    # flask
    flask \
    flask-restful \
    uwsgi \
    opencv-python \
    requests \
    Werkzeug \
 && python -m ipykernel.kernelspec

# configure console
RUN echo 'alias ll="ls --color=auto -lA"' >> /root/.bashrc \
 && echo '"\e[5~": history-search-backward' >> /root/.inputrc \
 && echo '"\e[6~": history-search-forward' >> /root/.inputrc

# dump package lists
RUN dpkg-query -l > /dpkg-query-l.txt \
&& pip2 freeze > /pip2-freeze.txt
