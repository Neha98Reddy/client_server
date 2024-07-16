import pika
import json
from pymongo import MongoClient
from flask import Flask, request, jsonify
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client.iot_data
collection = db.status

app = Flask(__name__)

def process_message(ch, method, properties, body):
    message = json.loads(body)
    message["timestamp"] = datetime.utcnow()
    collection.insert_one(message)

@app.route('/status_counts', methods=['GET'])
def status_counts():
    start_time = request.args.get('start')
    end_time = request.args.get('end')
    start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S')
    end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S')

    pipeline = [
        {"$match": {"timestamp": {"$gte": start_time, "$lte": end_time}}},
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ]

    result = list(collection.aggregate(pipeline))
    return jsonify(result)

def start_consuming():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='status_queue')

        channel.basic_consume(queue='status_queue', on_message_callback=process_message, auto_ack=True)
        print(' [*] Waiting for messages')
        channel.start_consuming()
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Could not connect to RabbitMQ: {e}")

if __name__ == "__main__":
    start_consuming()
    app.run(port=5000)
