import translationLayer
import transientSimulation
import constants

nominal_voltage_positive = constants.nominal_voltage_positve
nominal_voltage_negative = constants.nominal_voltage_negative
voltage_ripple_positive = constants.voltage_ripple_positive
voltage_ripple_negative = constants.voltage_ripple_negative

generation_resolution = translationLayer.generation_resolution

storage = transientSimulation.storage

deadtime_detector = []
deadtime_BCM = []

def read_current_amplitude(time): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = storage[int(time / generation_resolution)]
    return current_amplitude

def calc_deadtime_detector():
    time1 = 0
    while (time1 < (len(storage) * generation_resolution)):
        if (read_current_amplitude(time1) > (nominal_voltage_positive + voltage_ripple_positive)):
            deadtime_detector.append(read_current_amplitude(time1))
        elif (read_current_amplitude(time1) < (nominal_voltage_negative - voltage_ripple_negative)):
            deadtime_detector.append(read_current_amplitude(time1))
        time1 = time1 + generation_resolution

def calc_deadtime_BCM():
    time2 = 0
    while (time2 < (len(storage) * generation_resolution)):
        if (read_current_amplitude(time2) > (nominal_voltage_positive + voltage_ripple_positive)):
            deadtime_BCM.append(read_current_amplitude(time2))
        elif (read_current_amplitude(time2) < (nominal_voltage_negative - voltage_ripple_negative)):
            deadtime_BCM.append(read_current_amplitude(time2))
        time2 = time2 + generation_resolution