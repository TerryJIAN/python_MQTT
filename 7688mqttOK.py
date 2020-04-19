# coding: utf-8
import paho.mqtt.client as mqtt
import json
import serial
global s
s=serial.Serial("/dev/ttyS0", 57600,timeout = 0.2)

def on_connect(client, userdata, flags, rc):
         client.publish("Data", json.dumps({"username": user, "message": "Hello, anyone!"}))
         client.subscribe("Ctrl")
def on_message(client, userdata, msg):
         if  str(msg.payload):
#               s.write(str(msg.payload)+'\n')
                payload = json.loads(msg.payload.decode())
                s.write(str(payload.get("message"))+'\n')
if __name__=='__main__':
         client = mqtt.Client()
         client.on_connect = on_connect
         client.on_message = on_message

         HOST="192.168.212.150"
         client.connect(HOST, 1883, 60)

         user = "DUO"
         client.user_data_set(user)
         client.loop_start()
         while True:
                 str1= str(s.readline())
                 if (str1):
                         client.publish("Data", json.dumps({"username":"arduino", "message": str1}))