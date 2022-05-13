# Flask Template
<p align="center">
  <a href="https://www.rapidinnovation.io/" target="blank"><img src="static/images/ri_logo.jpeg" width="320" alt="RapidInnovation Logo" /></a>
</p>

Checkout *requirements.txt* for libraries used.

**Versions**
Python: 3.9.6

### Activate Virtual env
python -m venv venv
source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Run Flask Application
**Development Mode**

_python run.py_

or

flask run

**Run Flask via Gunicorn**

_gunicorn --bind 0.0.0.0:5000 wsgi:app_

**To Build Docker**
sudo docker-compose build
sudo docker-compose up

**Run -d to start container in background**
sudo docker-compose up -d

**To check status  of kafka or zookeeper**
sudo service kafka status
sudo service zookeeper status

**To start/stop  of kafka or zookeeper**
sudo service kafka start/stop
sudo service zookeeper start/stop

**To go inside of container**
sudo docker exec -it kafka /bin/sh

**To go inside of container otp/kafka**
cd /opt/kafka

**To create topics**
./bin/kafka-topics.sh --create --zookeeper zookeeper:2181
--replication-factor 1 --partitions 1 --topic my_first_topic

**To create topics with group name**
./bin/kafka-topics.sh --create --zookeeper zookeeper:2181
--replication-factor 1 --partitions 1 --topic my_first_topic -group give_group_id

**To check List of topics**
./bin/kafka-topics.sh --bootstrap-server=localhost:9092 --list

**To create Producer**
./bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic youtube

**To create Consumer**
./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic
youtube

**To check group id**
./bin/kafka-consumer-groups.sh --all-topics --bootstrap-server localhost:9092 --list 

**To describe group to get belonging consumers**
.bin/kafka-consumer-groups.sh --describe --group mygroup_name --bootstrap-server localhost:9092

**To kill container for some reason**
sudo docker container kill container_name

**To start/stop kafka/zookeeper inside of container**
sudo docker container start/stop kafka/zookeeper