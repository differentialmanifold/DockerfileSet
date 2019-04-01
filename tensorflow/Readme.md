# Tensorflow

Build a custom tensorflow environment.

```bash
sudo docker build -t my-tensorflow .
```

Then in project directory, you can run:

```bash
sudo docker run --rm -v $PWD:/tmp -w /tmp my-tensorflow python ./example.py --sum 1 2 3 4
```