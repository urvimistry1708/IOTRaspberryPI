from __future__ import print_function
#import context
import paho.mqtt.publish as publish
import psutil


channelID = "1278920" #change this channelID with your channelID
writeapiKey = "GZ2P37INRJ47BZVF" #Change this write API Key with your write API Key
useUnsecuredTCP = False
useSSLWebsockets = True
mqttHost = "mqtt.thingspeak.com"

if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':'/etc/ssl/certs/ca-certificates.crt','tls_version' : ssl.PROTOCOL_TLSv1}
    tPort = 443

topic = "channels/" + channelID + "/publish/" + writeapiKey
while(True):
    cpuPer = psutil.cpu_percent(interval=20)
    ramPer = psutil.virtual_memory().percent
    print("CPU= ",  cpuPer, " RAM: ", ramPer)
    tPayload = "field1=" + str(cpuPer) + "&field2=" + str(ramPer)
    try:
        publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
    except (KeyboardInterrupt):
        break
    except:
        print("There was an error while publishing the data")
