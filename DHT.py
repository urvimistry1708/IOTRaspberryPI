import sqlite3
import time
import board
import adafruit_dht
conn=sqlite3.connect('pir_db')
cursor=conn.cursor()
dhtDevice=adafruit_dht.DHT11(board.D4)
cursor.execute('create table IF NOT EXISTS DHTTEST (tempid INTEGER PRIMARY KEY AUTOINCREMENT ,tempretue INTEGER,humidity varchar(50))');

while True:
    try:
        tempretue=dhtDevice.temperature
        tempreture_f=tempretue*(9/5)+32
        humidity=dhtDevice.humidity
        print(int(tempretue),tempreture_f,humidity)
        cursor.execute("INSERT INTO DHTTEST (tempretue,humidity)values(?,?)",(int(tempretue),humidity))
        conn.commit()
            
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)

conn.close();