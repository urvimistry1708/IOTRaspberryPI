import context
import time
import paho.mqtt.client as mqtt
import sqlite3
DB = "mqttCPU"


conn = sqlite3.connect(DB)
curs = conn.cursor()


def on_message(client,userdata,msg):
  info =msg.payload.decode().split(',')
  print("CPU: "+info[0]+" RAM: "+info[1])
  sqlite_insert_with_param = """INSERT INTO TaskManager (cpu,ram) VALUES (?,?);"""
  data_tuple = (info[0],info[1])
  curs.execute(sqlite_insert_with_param, data_tuple)
  conn.commit();
	
client = mqtt.Client()
client.on_message = on_message
client.connect("broker.emqx.io",1883)
client.subscribe("mqtt1",qos=0)
client.loop_forever()
