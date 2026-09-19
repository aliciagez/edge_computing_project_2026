import paho.mqtt.client as mqtt
import json
from utils.connect_postgres import query_db

def on_message(client, userdata, message):
    payload = message.payload.decode()


    print("connect to mqtt", payload, flush=True)
    data = json.loads(payload)

    distance = data["distance"]

    query_db(
        """
        INSERT INTO distance_readings
        (time, distance)
        VALUES (NOW(), %s)
""",
        (distance,),
    )

    print(distance)

if __name__ == "__main__":
    query_db("""
        CREATE TABLE IF NOT EXISTS distance_readings (
            time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            distance DOUBLE PRECISION
            )
        """)

    client = mqtt.Client()
    client.connect("mosquitto", 1883)
    client.subscribe("home/pico/hc-sr04")
    client.on_message = on_message
    client.loop_forever()