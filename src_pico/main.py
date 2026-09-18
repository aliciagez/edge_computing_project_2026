import time
import json
from machine import Pin, PWM, freq
from wifi import connect_wifi
from umqtt.simple import MQTTClient

time.sleep(0.1) 

TOPIC = b"home/pico/hc-sr04"
MQTT_BROKER = "10.253.75.1"


trig =Pin(27, Pin.OUT)
echo =Pin(16, Pin.IN)
time.sleep(0.1) 

buzzer_pin=PWM(Pin(17))
buzzer_pin.duty_u16(0)

wifi_led = Pin(18, Pin.OUT)

pins = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
led_pin = [Pin(I, Pin.OUT) for I in pins]
total_led = len(led_pin)

def connect_mqtt():
    client = MQTTClient(client_id="pico", server = MQTT_BROKER, port=1883)
    client.connect()
    print("Connected to MQTT")
    return client


def echo_read_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    print("trig skickad")

    while echo.value() == 0:
        start = time.ticks_us()

    while echo.value() == 1:
        end = time.ticks_us()

    duration = time.ticks_diff(end, start)
    distance = (duration * 0.0343) / 2

    print(distance, "cm")
    time.sleep(0.5)

    return distance



def buzzer(distance):
    if distance >100:
        buzzer_pin.duty_u16(0)

    elif distance <=10:
        buzzer_pin.freq(2000)
        buzzer_pin.duty_u16(1000)
    
    elif distance <=20:
        buzzer_pin.freq(2000)
        buzzer_pin.duty_u16(1000) 
        time.sleep(0.05)       
        buzzer_pin.duty_u16(0) 
        time.sleep(0.05)

    elif distance <=50:
        buzzer_pin.freq(2000)
        buzzer_pin.duty_u16(1000) 
        time.sleep(0.5)       
        buzzer_pin.duty_u16(0) 
        time.sleep(0.5)
 
    else:
        buzzer_pin.freq(2000)
        buzzer_pin.duty_u16(1000)
        time.sleep(0.8)
        buzzer_pin.duty_u16(0)
        time.sleep(0.8)

        #for i in range(int(distance)):
            #buzzer_pin.freq(330)
            #buzzer_pin.duty_u16(100)         

def bar_graf(distance):
    if distance <= 0 or distance >100:
        light_on = 0
    elif int(distance // 10) + 1 > total_led:
        light_on = total_led

    else:
        light_on = int(distance // 10) + 1
        light_on = total_led - light_on

    for i in range(total_led):
        if i < light_on:
            led_pin[i].value(1)
        else:
            led_pin[i].value(0)


if __name__=="__main__":
    time.sleep(0.2)

    if connect_wifi():
        wifi_led.value(1)
        client = connect_mqtt()
    else:
        print("Not connected to wifi")

    while True:
        distance = echo_read_distance()
        bar_graf(distance)
        buzzer(distance)

        data = {"distance": distance}
        client.publish(TOPIC, json.dumps(data))