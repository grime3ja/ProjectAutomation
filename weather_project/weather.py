import python_weather

import asyncio
import os

from datetime import datetime

async def main():
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    weather = await client.get('Haymarket, Virginia')
    print(f"The current temperature in Haymarket is {weather.temperature}")

    min_temp = 150
    max_temp = -150
    for daily in weather:
      for hourly in daily:
        min_temp = min(int(hourly.temperature), min_temp)
        max_temp = max(int(hourly.temperature), max_temp)

    print(f"The high temperature today is {max_temp} and the low temperature is {min_temp}")

if __name__ == "__main__":
   asyncio.run(main())
