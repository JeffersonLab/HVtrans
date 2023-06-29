import math
from math import pi

nominal_voltage = 5 #nominal voltage of the wave
transient_voltage = 10 #transient voltage of the wave
voltage_ripple = 0.5 #voltage ripple in the wave at nominal voltage
nominal_frequency = 3 #wave frequency
transient_frequency = 1 #transient frequency
switching_frequency = 2 #switching frequency
aggression = 0.75 #arbitrary value to set the agression of the transient decay, zero equals no decay and one equals immediate decay

num_of_phases = 3 #number of phases per wave module
num_of_wave_modules = 3 #number of wave modules
increment_resolution = 0.01 #resolution with which the wave module is generated, measured in radians

nominal_angular_frequency = nominal_frequency * (2 * pi) #calculate the period of the wave in radians
transient_angular_frequency = transient_frequency * (2 * pi) #calculate the period of the transient in radians
switching_angular_frequency = switching_frequency * (2 * pi) #calculate the period of the switching in radians

nominal_period = 1 / nominal_frequency
transient_period = 1 / transient_frequency
switching_period = 1 / switching_frequency