# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


#broker = 'broker.emqx.io'
broker = 'broker.emqx.io'
port = 1883
#topic = "python/mqtt"
topic = "XuanKy/mqtt_test"


# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'

def connect_mqtt():
    '''
        #OLD VERSION 1.x
     def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    '''
        # New Version 2.0
    def on_connect(client, userdata, flags, reason_code, properties):
        if flags.session_present:
            pass
        if reason_code == 0:
            # success connect
            print("success_connect")
        if reason_code > 0:
            print("Fail_connect")


    #client = mqtt_client.Client(client_id)
    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()