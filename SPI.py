import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 115200
i = 0
while 1:
    print('-------------------------------')
    print(i)
    spi.writebytes([0x4, 0x061])
    time.sleep(1)
    resp = spi.readbytes(32)
    print(resp)