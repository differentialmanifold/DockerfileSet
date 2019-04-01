FROM tensorflow/tensorflow:1.13.1-py3

COPY . /tmp
WORKDIR /tmp
RUN pip install -i http://mirrors.tencentyun.com/pypi/simple --trusted-host mirrors.tencentyun.com -r requirements.txt

CMD ["/bin/bash"]