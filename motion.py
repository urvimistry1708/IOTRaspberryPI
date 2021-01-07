import RPi.GPIO as GPIO
import time
import sys
import sqlite3

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.IN)
GPIO.setup(24,GPIO.OUT);

DB_NAM = "motion_db"

conn = sqlite3.connect(DB_NAM)
curs = conn.cursor()

curs.execute('create table IF NOT EXISTS motions(motion_id INTEGER PRIMARY KEY AUTOINCREMENT,mtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,message VARCHAR(50))');
while True:
    i = GPIO.input(18)
    if i ==0:
        print("NO ANY MOTION");
        time.sleep(1);
    if i ==1:
        curs.execute("INSERT INTO MOTIONS(message) values('motion detected')");
        conn.commit();
        print("motion detected")
        GPIO.output(24,1);
        time.sleep(5);
        GPIO.output(24,0);
        
conn.close()