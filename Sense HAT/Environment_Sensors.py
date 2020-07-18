from sense_hat import SenseHat

sense = SenseHat()

print('\n\t[*] Current Humidity: %s %%rh' %round(sense.get_humidity()))
print('\n\t[*] Current Temperature: %s Celsius' %round(sense.get_temperature()))
print('\n\t[*] Current Pressure: %s Milibars\n' %round(sense.get_pressure()))