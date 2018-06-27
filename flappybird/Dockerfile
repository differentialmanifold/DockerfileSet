FROM tensorflow/tensorflow:1.8.0-py3

COPY . /flappybird

WORKDIR /flappybird

RUN pip3 --no-cache-dir install \
        scikit-image \
        pygame

# TensorBoard
EXPOSE 6006

EXPOSE 8888

CMD ["/bin/bash"]