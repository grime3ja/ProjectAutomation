import python_weather

import asyncio
import os
import sys

from datetime import datetime
import time

async def main():
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    weather = None
    while True:
      try:
        weather = await client.get('Haymarket, Virginia')
      except Exception as e:
        continue
      if weather is not None:
        break
    print(f"The current temperature in Haymarket is {weather.temperature}°F. ")
 
    min_temp = 150
    max_temp = -150
    rain_times = []
    start_time = ""
    end_time = ""
    for hourly in weather.daily_forecasts[0].hourly_forecasts:
      min_temp = min(int(hourly.temperature), min_temp)
      max_temp = max(int(hourly.temperature), max_temp)
      if "rain" in hourly.description.lower():
        if not start_time:
          start_time = hourly.time
      elif start_time:
        end_time = hourly.time
        rain_times.append((start_time, end_time))
        start_time = ""
      
    print(f"The high temperature today is {max_temp}°F, and the low temperature is {min_temp}°F. ")

    for start, end in rain_times:
      print(f"Rain starting at {start.strftime("%I:%M:%S %p")}, and ending at {end.strftime("%I:%M:%S %p")}. ")
    if start_time:
      print(f"Rain starting at {start_time.strftime("%I:%M:%S %p")}, and going through to the end of the day. ")

if __name__ == "__main__":
  asyncio.run(main())

