#import context
import time
import paho.mqtt.client as mqtt

def on_message(client,userdata,msg):
	print(msg.topic+" "+str(msg.payload)+"\n")
	decodeData = msg.payload.decode("utf-8")
	print(decodeData)
	
client = mqtt.Client()
client.on_message = on_message
client.connect("broker.emqx.io",1883)
client.subscribe("mqtt1",qos=0)
client.loop_forever()
