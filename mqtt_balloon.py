import ssl
import paho.mqtt.client as mqtt

broker_address = "https://eu1.cloud.thethings.network/console/applications/coreconf"
username= "coreconf@ttn"
password = ""

broker_address = "eu1.cloud.thethings.network"
client_id = "Client1"
topic = "v3/coreconf@ttn/devices/+/up"

broker_port = 8883

#client = mqtt.Client(client_id, protocol=mqtt.MQTTv5)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS, ciphers=None)

client.username_pw_set(username, password)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
          + message.topic + "' with QoS " + str(message.qos))


client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port)
client.subscribe(topic)

client.loop_forever()

