import translationLayer
import transientSimulation
import samplingSimulation

transient_voltage_positive = translationLayer.transient_voltage_positive
transient_voltage_negative = translationLayer.transient_voltage_negative
nominal_voltage_positive = translationLayer.nominal_voltage_positve
nominal_voltage_negative = translationLayer.nominal_voltage_negative

generation_resolution = translationLayer.generation_resolution

storage = transientSimulation.storage

BCM_pos_transient_voltage = 0
BCM_neg_transient_voltage = 0

detector_pos_transient_voltage = 0
detector_neg_transient_voltage = 0

def read_current_amplitude_detector(time): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = storage[int(time / generation_resolution)]
    return current_amplitude

def read_current_amplitude_BCM(time , BCM_resolution , BCM_storage): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = BCM_storage[int(time / BCM_resolution)]
    return current_amplitude

def BCM_transient_voltage_calculator(BCM_resolution , BCM_storage):
    time1 = 0
    global BCM_pos_transient_voltage
    global BCM_neg_transient_voltage

    BCM_pos_transient_voltage = 0
    BCM_neg_transient_voltage = 0

    while (time1 < (len(BCM_storage) * BCM_resolution)):
        if (BCM_pos_transient_voltage <= read_current_amplitude_BCM(time1 , BCM_resolution , BCM_storage)):
            BCM_pos_transient_voltage = read_current_amplitude_BCM(time1 , BCM_resolution , BCM_storage)
        elif (BCM_neg_transient_voltage <= abs(read_current_amplitude_BCM(time1 , BCM_resolution , BCM_storage))):
            BCM_neg_transient_voltage = abs(read_current_amplitude_BCM(time1 , BCM_resolution , BCM_storage))
        time1 = time1 + BCM_resolution

def detector_transient_voltage_calculator():
    time2 = 0
    global detector_pos_transient_voltage
    global detector_neg_transient_voltage

    detector_pos_transient_voltage = 0
    detector_neg_transient_voltage = 0

    while (time2 < (len(storage) * generation_resolution)):
        if (detector_pos_transient_voltage <= read_current_amplitude_detector(time2)):
            detector_pos_transient_voltage = read_current_amplitude_detector(time2)
        elif (detector_neg_transient_voltage <= abs(read_current_amplitude_detector(time2))):
            detector_neg_transient_voltage = abs(read_current_amplitude_detector(time2))
        time2 = time2 + generation_resolution

def calc_total_asymmetry():
    global BCM_pos_transient_voltage
    global BCM_neg_transient_voltage

    global detector_pos_transient_voltage
    global detector_neg_transient_voltage

    input_asymmetry = (detector_pos_transient_voltage - detector_neg_transient_voltage)

    systematic_error = (abs((detector_pos_transient_voltage / BCM_pos_transient_voltage) - (detector_neg_transient_voltage / BCM_neg_transient_voltage)) / ((detector_pos_transient_voltage / BCM_pos_transient_voltage) + (detector_neg_transient_voltage / BCM_neg_transient_voltage)))
    return systematic_error