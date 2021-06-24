import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "zxdqt4",
        "typeId": "sagar",
        "deviceId":"Sagarjillela"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    print()
    if(m=="LIGHTON"):
        print("light is turned on")
    elif(m=="LIGHTOFF"):
        print("light is turned off")
    print()

              

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    sunlight=random.randint(0,400)
    maxintensity=200
    
    
    print()
    if(maxintensity<sunlight):

        p=print("light is off")
    elif(maxintensity==sunlight):
        p=print("intensity=100")
    elif(maxintensity>sunlight):
        p=print("intensity=150")
    elif(sunlight==0):
        p=print("light is at maxintensity")
    print()
    myData={'d':{'sunlight':sunlight}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
