import translationLayer
import transientSimulation
import samplingSimulation
import scipy

nominal_voltage_negative = translationLayer.nominal_voltage_negative

transient_period_positive = translationLayer.transient_period_positive
transient_period_negative = translationLayer.transient_period_negative
switching_period = translationLayer.switching_period

deadtime_width_detector = translationLayer.deadtime_width_detector
deadtime_shift_detector = translationLayer.deadtime_shift_detector
deadtime_width_BCM = translationLayer.deadtime_width_BCM
deadtime_shift_BCM = translationLayer.deadtime_shift_BCM

generation_resolution = translationLayer.generation_resolution

storage = transientSimulation.storage

no_deadtime_detector = [] #list used for the detector's deadtime graph generation
pos_detector = []
neg_detector = []

no_deadtime_BCM = [] #list used for the BCM's deadtime graph generation
pos_BCM = []
neg_BCM = []

def read_current_amplitude_detector(time): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = storage[int(time / generation_resolution)]
    return current_amplitude

def read_current_amplitude_BCM(time , BCM_resolution , BCM_storage): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = BCM_storage[int(time / BCM_resolution)]
    return current_amplitude

def calc_deadtime_detector(): #samples the original wave to create an array modelling its deadtime
    time1 = 0

    while (time1 < (len(storage) * generation_resolution)):
        if (transient_period_positive < time1 < switching_period):
            no_deadtime_detector.append(read_current_amplitude_detector(time1))
            pos_detector.append(read_current_amplitude_detector(time1))

        elif (switching_period + transient_period_negative < time1):
            no_deadtime_detector.append(read_current_amplitude_detector(time1))
            neg_detector.append(read_current_amplitude_detector(time1) + (2 * nominal_voltage_negative))
        time1 = time1 + generation_resolution
    print('Detector Deadtime Measurement Finished')

def calc_deadtime_BCM(BCM_resolution , BCM_storage): #samples the BCM wave to create an array modelling its deadtime
    time2 = 0

    while (time2 < (len(BCM_storage) * BCM_resolution)):
        if (transient_period_positive < time2 < switching_period + transient_period_negative):
            no_deadtime_BCM.append(read_current_amplitude_BCM(time2 , BCM_resolution , BCM_storage))
            pos_BCM.append(read_current_amplitude_BCM(time2 , BCM_resolution , BCM_storage))

        elif (switching_period + 2 * transient_period_negative < time2):
            no_deadtime_BCM.append(read_current_amplitude_BCM(time2 , BCM_resolution , BCM_storage))
            neg_BCM.append(read_current_amplitude_BCM(time2 , BCM_resolution , BCM_storage) + (2 * nominal_voltage_negative))
        time2 = time2 + BCM_resolution