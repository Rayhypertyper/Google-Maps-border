## Overview
This project uses the Google Maps API to calculate travel times for a route crossing from Canada into the United States. It locates the closest border crossings, retrieves estimated wait times, and prints out a final summary table of travel details.

## Features
- Prompts for origin, destination, and departure hour.
- Provides travel time through multiple different borders.
- Outputs a formatted table with new travel time, considering border delays.


## Requirements
- Python 3.7+  
- Google Maps Python client (`pip install googlemaps`)  
- Tabulate (`pip install tabulate`)  
- Additional custom modules:  
  - [data.py → `navigate_website`]  
  - [scrape.py → `find_wait_times`]

## Setup
- In main.py, enter your Google Maps API code
- Run main.py
