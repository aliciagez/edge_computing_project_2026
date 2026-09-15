import time
from machine import Pin, PWM, freq

time.sleep(0.1) 


trig =Pin(13, Pin.OUT)
echo =Pin(15, Pin.IN)
time.sleep(0.1) 

buzzer_pin=PWM(Pin(11))
buzzer_pin.duty_u16(0)

pins = [16, 17, 18, 19, 20, 21, 22, 26, 27, 28]
led_pin = [Pin(I, Pin.OUT) for I in pins]
total_led = len(led_pin)



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


def bar_graf(distance):
    if distance <= 0 or distance >100:
        light_on = 0
    elif int(distance // 10) + 1 > total_led:
        light_on = total_led

    else:
        light_on = int(distance // 10) + 1

    for i in range(total_led):
        if i < light_on:
            led_pin[i].value(1)
        else:
            led_pin[i].value(0)


def buzzer(distance):
    if distance <=50:
        buzzer_pin.freq(330)
        buzzer_pin.duty_u16(100) 
     
    else:
        buzzer_pin.duty_u16(0)



if __name__=="__main__":
    while True:
        distance = echo_read_distance()
        bar_graf(distance)
        buzzer(distance)

        time.sleep(1)



