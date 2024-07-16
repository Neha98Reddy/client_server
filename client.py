import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print(f"Failed to connect, return code {rc}")
        
def connect_mqtt():
    client = mqtt.Client(client_id="client1", protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    try:
        client.connect("localhost", 4369, 60)
    except ConnectionRefusedError:
        print("Connection refused, retrying...")
        time.sleep(5)  
        connect_mqtt()  

    client.loop_forever()

if __name__ == "__main__":
    connect_mqtt()
