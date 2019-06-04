# Tomcat

setenv.sh used to set jvm parameters.
catalina.properties used to set shared.loader.

```bash
sudo docker run -d --rm -p 8888:8080 \
-v ~/tomcat/bin/setenv.sh:/usr/local/tomcat/bin/setenv.sh \
-v ~/tomcat/conf/catalina.properties:/user/local/tomcat/conf/catalina.properties \
-v ~/tomcat/webapps:/usr/local/tomcat/webapps \
-v ~/tomcat/logs:/usr/local/tomcat/logs tomcat
```