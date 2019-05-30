# Tomcat

setenv.sh used to set jvm parameters.

```bash
sudo docker run -d --rm -p 8888:8080 \
-v ~/tomcat/bin/setenv.sh:/usr/local/tomcat/bin/setenv.sh \
-v ~/tomcat/webapps:/usr/local/tomcat/webapps \
-v ~/tomcat/logs:/usr/local/tomcat/logs tomcat
```