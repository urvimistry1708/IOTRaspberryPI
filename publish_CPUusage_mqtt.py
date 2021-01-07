import context
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import psutil
	
client = mqtt.Client()
client.connect("broker.emqx.io",1883,60)
while True:
    cpuPer = psutil.cpu_percent(interval=20)
    ramPer = psutil.virtual_memory().percent
    print("CPU= ",  cpuPer, " RAM: ", ramPer)
    
    tPayload =str(cpuPer)+","+str(ramPer)
    client.publish(topic="mqtt1",payload=tPayload,qos=0,retain=False)
client.loop_forever()
