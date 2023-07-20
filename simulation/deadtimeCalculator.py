import constants
import translationLayer
import transientSimulation
import samplingSimulation

nominal_voltage_positive = constants.nominal_voltage_positve
nominal_voltage_negative = constants.nominal_voltage_negative
voltage_ripple_positive = constants.voltage_ripple_positive
voltage_ripple_negative = constants.voltage_ripple_negative

generation_resolution = translationLayer.generation_resolution
BCM_resolution = samplingSimulation.BCM_resolution
BCM_resolution = 1 / BCM_resolution #converts the resolution from measurements per seconds to seconds per measurement

storage = transientSimulation.storage
BCM_storage = samplingSimulation.BCM_storage

deadtime_detector = [] #list used for the detector's deadtime graph generation
deadtime_BCM = [] #list used for the BCM's deadtime graph generation

def read_current_amplitude_detector(time): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = storage[int(time / generation_resolution)]
    return current_amplitude

def read_current_amplitude_BCM(time): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = BCM_storage[int(time / BCM_resolution)]
    return current_amplitude

def calc_deadtime_detector(): #samples the original wave to create an array modelling its deadtime
    time1 = 0
    while (time1 < (len(storage) * generation_resolution)):
        if (read_current_amplitude_detector(time1) > (nominal_voltage_positive + voltage_ripple_positive)):
            deadtime_detector.append(1)
        elif (read_current_amplitude_detector(time1) < (-nominal_voltage_negative - voltage_ripple_negative)):
            deadtime_detector.append(1)
        else:
            deadtime_detector.append(0)
        time1 = time1 + generation_resolution

def calc_deadtime_BCM(): #samples the BCM wave to create an array modelling its deadtime
    time2 = 0
    while (time2 < (len(BCM_storage) * BCM_resolution)):
        if (read_current_amplitude_BCM(time2) > (nominal_voltage_positive + voltage_ripple_positive)):
            deadtime_BCM.append(1)
        elif (read_current_amplitude_BCM(time2) < (-nominal_voltage_negative - voltage_ripple_negative)):
            deadtime_BCM.append(1)
        else:
            deadtime_BCM.append(0)
        time2 = time2 + BCM_resolution