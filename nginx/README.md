# Nignx

```bash

sudo docker pull nginx

mkdir -p ~/nginx/config ~/nginx/www ~/nginx/logs

sudo docker run --name my-nginx --rm -d -p 8080:8080 -v ~/nginx/config/nginx.conf:/etc/nginx/nginx.conf:ro -v ~/nginx/config/certs:/etc/nginx/certs -v ~/nginx/www/:/var/www/ -v ~/nginx/logs/:/var/log/nginx/ nginx

```