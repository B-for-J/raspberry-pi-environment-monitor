import Adafruit_DHT

SENSOR = Adafruit_DHT.DHT22
PIN = 4  # GPIO pin

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)

    if humidity is None or temperature is None:
        raise RuntimeError("Failed to read from sensor")

    return round(temperature, 2), round(humidity, 2)
