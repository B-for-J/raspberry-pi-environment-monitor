# raspberry-pi-environment-monitor
A Python-based Raspberry Pi project that monitors temperature and humidity using a DHT sensor.
The system logs data locally and demonstrates basic hardware–software integration.

## Features
- Reads temperature and humidity from a DHT22 sensor
- Logs data with timestamps to a CSV file
- Handles sensor read errors gracefully
- Designed for easy extension (OLED display, alerts, web dashboard)

## Hardware
- Raspberry Pi
- DHT22 (or DHT11) sensor

## How It Works
The program reads sensor data at fixed intervals, prints live readings, and stores the data for later analysis.

## Future Improvements
- Web-based dashboard
- OLED display output
- Email or Telegram alerts
