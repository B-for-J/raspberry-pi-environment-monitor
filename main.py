import time
from sensor import read_sensor
from logger import log_data

INTERVAL = 5  # seconds

def main():
    print("Starting Environment Monitor...")
    
    while True:
        try:
            temp, humidity = read_sensor()
            log_data(temp, humidity)
            print(f"Temp: {temp}°C | Humidity: {humidity}%")
        except Exception as e:
            print("Error:", e)

        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
