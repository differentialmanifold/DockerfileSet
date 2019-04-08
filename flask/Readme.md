# Flask

my_tensorflow is the image build on tensorflow/tensorflow:1.13.1-py3 with flask, flask-cors installed.

```bash

sudo docker run --name my-flask --rm -d -p 5000:5000 -v $PWD:/tmp -w /tmp my-tensorflow /bin/bash -c "export FLASK_APP=app.py;flask run --host=0.0.0.0 --port=5000 --with-threads"

```

Query with curl

```bash
curl http://localhost:5000/hello

curl -H "Content-Type: application/json" -d '{"instances": [[1.0, 2.0]]}' \
    -X POST http://localhost:5000/hello_post
```