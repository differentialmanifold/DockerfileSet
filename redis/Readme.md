# Redis

redis.conf under conf directory, and dump.rdb under data directory.

```bash
sudo docker run --rm --network=host -d -v ~/redis/conf/redis.conf:/usr/local/etc/redis/redis.conf -v ~/redis/data:/data --name myredis redis redis-server /usr/local/etc/redis/redis.conf

sudo docker run -it --network=host --rm redis redis-cli 
```