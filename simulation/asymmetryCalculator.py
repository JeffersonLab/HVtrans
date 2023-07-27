import translationLayer
import transientSimulation
import samplingSimulation

nominal_voltage_positive = translationLayer.nominal_voltage_positve
nominal_voltage_negative = translationLayer.nominal_voltage_negative
voltage_ripple_positive = translationLayer.voltage_ripple_positive
voltage_ripple_negative = translationLayer.voltage_ripple_negative

generation_resolution = translationLayer.generation_resolution
BCM_resolution = translationLayer.BCM_resolution

storage = transientSimulation.storage
BCM_storage = samplingSimulation.BCM_storage

BCM_pos_period = 0
BCM_neg_period = 0

detector_pos_period = 0
detector_neg_period = 0

def read_current_amplitude_detector(time): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = storage[int(time / generation_resolution)]
    return current_amplitude

def read_current_amplitude_BCM(time): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = BCM_storage[int(time / BCM_resolution)]
    return current_amplitude

def BCM_periods_calculator():
    time1 = 0
    global BCM_pos_period
    global BCM_neg_period
    tracker = 1
    if (BCM_resolution > 0.000001):
        acceptable_error = 22500000 * BCM_resolution
    else:
        acceptable_error = 0.000000001
    
    lower_pos = nominal_voltage_positive + voltage_ripple_positive - acceptable_error
    upper_pos = nominal_voltage_positive + voltage_ripple_positive
    lower_neg = -nominal_voltage_negative - voltage_ripple_negative + acceptable_error
    upper_neg = -nominal_voltage_negative - voltage_ripple_negative
    while (time1 < (len(BCM_storage) * BCM_resolution)):
        if (lower_pos <= read_current_amplitude_BCM(time1) <= upper_pos and tracker == 1):
            BCM_pos_period = ((4 / 3) * time1) - 0.0000102
            print(time1)
            tracker = tracker + 1
        elif (upper_neg <= read_current_amplitude_BCM(time1) <= lower_neg and tracker == 2 and time1 > 0.000531):
            BCM_neg_period = (4 * time1) - 0.0005310365
            tracker = tracker + 1
        time1 = time1 + generation_resolution

def detector_periods_calculator():
    time2 = 0
    global detector_pos_period
    global detector_neg_period
    tracker = 1
    acceptable_error = 0.000000001

    lower_pos = nominal_voltage_positive + voltage_ripple_positive - acceptable_error
    upper_pos = nominal_voltage_positive + voltage_ripple_positive
    lower_neg = -nominal_voltage_negative - voltage_ripple_negative + acceptable_error
    upper_neg = -nominal_voltage_negative - voltage_ripple_negative
    while (time2 < (len(storage) * generation_resolution)):
        if (lower_pos <= read_current_amplitude_detector(time2) <= upper_pos and tracker == 1):
            detector_pos_period = ((4 / 3) * time2) - 0.0000102
            tracker = tracker + 1
        elif (upper_neg <= read_current_amplitude_detector(time2) <= lower_neg and tracker == 2 and time2 > 0.000531):
            detector_neg_period = (4 * time2) - 0.000531036
            tracker = tracker + 1
        time2 = time2 + generation_resolution

def calc_total_asymmetry():
    global BCM_pos_period
    global BCM_neg_period

    global detector_pos_period
    global detector_neg_period

    frequency_pos_wave_BCM = 1 / BCM_pos_period
    frequency_neg_wave_BCM = 1 / BCM_neg_period

    frequency_pos_wave_detector = 1 / detector_pos_period
    frequency_neg_wave_detector = 1 / detector_neg_period

    print(frequency_pos_wave_BCM , frequency_neg_wave_BCM)

    total_asymmetry = (((frequency_pos_wave_detector / frequency_pos_wave_BCM) - (frequency_neg_wave_detector / frequency_neg_wave_BCM)) / ((frequency_pos_wave_detector / frequency_pos_wave_BCM) + (frequency_neg_wave_detector / frequency_neg_wave_BCM)))
    return total_asymmetry