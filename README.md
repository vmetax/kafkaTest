# kafkaTest
using docker-compose run the following command
docker-compose -f docker-compose-expose.yml up -d # it will run in background

using "docker cp" command copy all files into docker container e.g.
docker cp kafkaTest.py 5fd2c1e3ea70:/root

then run the following command
docker exec -it kafka /bin/sh 

into docker container install python and python modules (Linux Alpine):
apk add python3
apk add py3-pip
pip install kafka-python

In order to run the test use the following command:
python3 test.py
