FROM tensorflow/tensorflow:1.8.0-py3

RUN apt-get update && apt-get install -y --no-install-recommends \
        python-numpy \
        python-dev \
        cmake \
        zlib1g-dev \
        libjpeg-dev \
        xvfb \
        libav-tools \
        xorg-dev \
        python-opengl \
        libboost-all-dev \
        libsdl2-dev \
        swig \
        python3-tk \
        vim

RUN pip3 install 'gym[all]'

# TensorBoard
EXPOSE 6006

EXPOSE 8888

#CMD ["/run_jupyter.sh", "--allow-root"]

CMD ["/bin/bash"]

