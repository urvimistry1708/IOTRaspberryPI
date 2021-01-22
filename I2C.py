from smbus import SMBus

addr = 0x8#arduino Address
bus = SMBus(1)#indicates /dev/i2c-1

numb = 1

print("Enter 1 for ON or 0 for OFF")
while numb == 1:
    ledstate = "1"
    if ledstate == "1":
        bus.write_byte(addr, 0x1)#(0x1=on)
        block = bus.read_byte_data(8,1)#(same as 0x8 address,cnt of data)
        print(block)
    elif ledstate == "0":
        bus.write_byte(addr, 0x0)#(0x0=led off)
    else:
        numb = 0
