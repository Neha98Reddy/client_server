Prerequisites

1. RabbitMQ: Ensure RabbitMQ is installed and running.
2. MongoDB: Ensure MongoDB is installed and running.
3. Python: Ensure Python is installed (preferably Python 3.6+).
4. Required Python Libraries:
   - `paho-mqtt`
   - `pika`
   - `pymongo`
   - `flask`


### pip install paho-mqtt pika pymongo flask


### Setting Up RabbitMQ with MQTT Plugin

1. Install RabbitMQ:
   Download and install RabbitMQ from the official [RabbitMQ download page](https://www.rabbitmq.com/download.html).

2. Enable MQTT Plugin:
   Open a terminal with administrative privileges and run:
   
   ### rabbitmq-plugins enable rabbitmq_mqtt
   

3. Start RabbitMQ:
   Make sure RabbitMQ is running:
   
   ### rabbitmq-service start
   ```

Client Script (`client.py`)

The client script will emit MQTT messages every second with a random "status" value between 0 and 6.

### Server Script (`server.py`)

The server script will consume messages from RabbitMQ and store them in MongoDB.

### Running the Scripts

1. Run RabbitMQ:
   Ensure RabbitMQ is running. Use `rabbitmq-service start` if not running.

2. Run MongoDB:
   Ensure MongoDB is running. Use `mongod` to start the MongoDB server if not running.


### Data Retrieval Endpoint

The server provides an endpoint `/status_count` to retrieve the count of each status within a specified time range. You can access it as follows:

```
http://localhost:5000/status_count?start_time=2024-07-15%2000:00:00&end_time=2024-07-15%2023:59:59
```

