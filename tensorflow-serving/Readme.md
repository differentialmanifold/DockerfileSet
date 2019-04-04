# Tensorflow-serving

Start TensorFlow Serving container and open the gRPC port and the REST API port

```bash
sudo docker run -t --rm -p 8500:8500 -p 8501:8501 \
  -v ~/tensorflow-serving/models:/models \
  tensorflow/serving --model_config_file=/models/models.config &
```

Query the model using the predict API

```bash
curl -d '{"instances": [[1.0, 2.0]]}' \
    -X POST http://localhost:8501/v1/models/add_and_multiple_two:predict
```