# Automated Parking Lot 

### What and Why
A simple console based parking lot simulation application developed as solution to a coding test.

### Where and How
It was developed on Ubuntu 18.04 in WSL using Python 3.6.8. The only additional package it uses is [Click](https://click.palletsprojects.com/en/7.x/).
The _demo.gif_ shows how to use the application on your system. 
Example: `python main.py create-parking-lot 6`

### Short description of the methods
- `create-parking-lot INTEGER`: Create a new parking lot with INTEGER number of empty lots
- `park REG_NO COLOR`: Parks a vehicle with the registration number REG_NO and color COLOR
- `leave INTEGER`: Empties parking slot number INTEGER
- `status`: Show the current status of the parking lot in a tabular manner
- `registration-numbers-for-cars-with-colour COLOR`: Returns registration numbers of all the vehicles with the color COLOR
- `slot-numbers-for-cars-with-colour COLOR`: Returns parked slot numbers for all the vehicles with the color COLOR
- `slot-number-for-registration-number REG_NO`: Returns parked slot number for the vehicle with the registration number REG_NO
