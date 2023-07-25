import constants
import translationLayer
import transientSimulation
import samplingSimulation

nominal_voltage_positive = constants.nominal_voltage_positve
nominal_voltage_negative = constants.nominal_voltage_negative
voltage_ripple_positive = constants.voltage_ripple_positive
voltage_ripple_negative = constants.voltage_ripple_negative

deadtime_width_detector = translationLayer.deadtime_width_detector
deadtime_shift_detector = translationLayer.deadtime_shift_detector
deadtime_width_BCM = translationLayer.deadtime_width_BCM
deadtime_shift_BCM = translationLayer.deadtime_shift_BCM

generation_resolution = translationLayer.generation_resolution

storage = transientSimulation.storage
BCM_storage = samplingSimulation.BCM_storage

deadtime_detector = [] #list used for the detector's deadtime graph generation
deadtime_BCM = [] #list used for the BCM's deadtime graph generation

length_deadtime_detector = [] #list used for the length of dectector's deadtime
length_deadtime_BCM = [] #list used for the length of BCM's deadtime

def read_current_amplitude_detector(time): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = storage[int(time / generation_resolution)]
    return current_amplitude

def read_current_amplitude_BCM(time , BCM_resolution): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = BCM_storage[int(time / BCM_resolution)]
    return current_amplitude

def calc_deadtime_detector(): #samples the original wave to create an array modelling its deadtime
    time1 = 0
    time2 = 0
    if (deadtime_shift_detector > 0):
        while (time1 < deadtime_shift_detector):
            deadtime_detector.append(0)
            time1 = time1 + generation_resolution
        time2 = time2 + deadtime_shift_detector

    while (time2 < (len(storage) * generation_resolution)):
        if (read_current_amplitude_detector(time2) > (nominal_voltage_positive + voltage_ripple_positive)):
            deadtime_detector.append(1)
        elif (read_current_amplitude_detector(time2) < (-nominal_voltage_negative - voltage_ripple_negative)):
            deadtime_detector.append(1)
        else:
            deadtime_detector.append(0)
        time2 = time2 + generation_resolution

    if (deadtime_shift_detector < 0):
        del deadtime_detector[:int(-deadtime_shift_detector / generation_resolution)]
        while (time1 > deadtime_shift_detector):
            deadtime_detector.append(0)
            time1 = time1 - generation_resolution
    print('Detector Deadtime Measurement Finished')

def calc_deadtime_BCM(BCM_resolution): #samples the BCM wave to create an array modelling its deadtime
    time3 = 0
    time4 = 0
    BCM_resolution = 1 / BCM_resolution #converts the resolution from measurements per seconds to seconds per measurement
    if (deadtime_shift_BCM > 0):
        while (time3 < deadtime_shift_BCM):
            deadtime_BCM.append(0)
            time3 = time3 + BCM_resolution
        time4 = time4 + deadtime_shift_BCM

    while (time4 < (len(BCM_storage) * BCM_resolution)):
        if (read_current_amplitude_BCM(time4 , BCM_resolution) > (nominal_voltage_positive + voltage_ripple_positive)):
            deadtime_BCM.append(1)
        elif (read_current_amplitude_BCM(time4 , BCM_resolution) < (-nominal_voltage_negative - voltage_ripple_negative)):
            deadtime_BCM.append(1)
        else:
            deadtime_BCM.append(0)
        time4 = time4 + BCM_resolution

    if (deadtime_shift_BCM < 0):
        del deadtime_BCM[:int(-deadtime_shift_BCM / BCM_resolution)]
        while (time3 > deadtime_shift_BCM):
            deadtime_BCM.append(0)
            time3 = time3 - BCM_resolution

def read_current_amplitude_deadtime_detector(time): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = deadtime_detector[int(time / generation_resolution)]
    return current_amplitude

def read_current_amplitude_deadtime_BCM(time , BCM_resolution): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = deadtime_BCM[int(time / BCM_resolution)]
    return current_amplitude

def calc_length_deadtime_detector():
    calc_deadtime_detector()
    time5 = 0
    while (time5 < (len(deadtime_detector) * generation_resolution)):
        if(read_current_amplitude_deadtime_detector(time5) > 0):
            length_deadtime_detector.append(0)
        time5 = time5 + generation_resolution

def calc_length_deadtime_BCM(BCM_resolution):
    calc_deadtime_BCM(BCM_resolution)
    time6 = 0
    BCM_resolution = 1 / BCM_resolution #converts the resolution from measurements per seconds to seconds per measurement
    while (time6 < (len(deadtime_BCM) * BCM_resolution)):
        if(read_current_amplitude_deadtime_BCM(time6, BCM_resolution) > 0):
            length_deadtime_BCM.append(0)
        time6 = time6 + BCM_resolution