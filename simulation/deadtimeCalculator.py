import translationLayer
import transientSimulation
import samplingSimulation

nominal_voltage_positive = translationLayer.nominal_voltage_positve
nominal_voltage_negative = translationLayer.nominal_voltage_negative
voltage_ripple_positive = translationLayer.voltage_ripple_positive
voltage_ripple_negative = translationLayer.voltage_ripple_negative

deadtime_width_detector = translationLayer.deadtime_width_detector
deadtime_shift_detector = translationLayer.deadtime_shift_detector
deadtime_width_BCM = translationLayer.deadtime_width_BCM
deadtime_shift_BCM = translationLayer.deadtime_shift_BCM

generation_resolution = translationLayer.generation_resolution
BCM_resolution = translationLayer.BCM_resolution

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

def calc_deadtime_BCM(): #samples the BCM wave to create an array modelling its deadtime
    time3 = 0
    time4 = 0
    if (deadtime_shift_BCM > 0):
        while (time3 < deadtime_shift_BCM):
            deadtime_BCM.append(0)
            time3 = time3 + BCM_resolution
        time4 = time4 + deadtime_shift_BCM

    while (time4 < (len(BCM_storage) * BCM_resolution)):
        if (read_current_amplitude_BCM(time4) > (nominal_voltage_positive + voltage_ripple_positive)):
            deadtime_BCM.append(1)
        elif (read_current_amplitude_BCM(time4) < (-nominal_voltage_negative - voltage_ripple_negative)):
            deadtime_BCM.append(1)
        else:
            deadtime_BCM.append(0)
        time4 = time4 + generation_resolution

    if (deadtime_shift_BCM < 0):
        del deadtime_BCM[:int(-deadtime_shift_BCM / BCM_resolution)]
        while (time3 > deadtime_shift_BCM):
            deadtime_BCM.append(0)
            time3 = time3 - BCM_resolution