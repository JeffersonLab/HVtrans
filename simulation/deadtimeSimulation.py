#scan through light state generation (storage) array and find any value greater nominal_voltage + voltage_ripple
#if true, append one
#else, append zero

import translationLayer
import transientSimulation

generation_resolution = translationLayer.generation_resolution
voltage_ripple_positive = translationLayer.voltage_ripple_positive
voltage_ripple_negative = translationLayer.voltage_ripple_negative
voltage_ripple_average = (voltage_ripple_positive + voltage_ripple_negative) / 2

storage = transientSimulation.storage

deadtime = [] #list used for deadtimeSimulation generation

def calc_deadtime(width , offset):
    time = 0
    while (time < len(storage)):
        current_amplitude = transientSimulation.read_current_amplitude(time)
        if (current_amplitude < voltage_ripple_average):
            deadtime.append(0)
        else: 
            int_time = 0
            while(int_time < width):
                deadtime.append(1)
                time = time + 1
                int_time = int_time + generation_resolution

#add offset