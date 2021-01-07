import context
import paho.mqtt.client as mqtt
import time


def on_connect(client,userdata,flags,rc):
  print(f"Connected with result code {rc}")
client=mqtt.Client()
client.on_connect=on_connect
client.connect("broker.emqx.io",1883,60)

for i in range(5):
 client.publish(topic='mqtt1',payload="hello subscriber!!",qos=0,retain=False)
 print(f"Send {i} to raspberry/topic")
 time.sleep(1)
client.loop_forever()