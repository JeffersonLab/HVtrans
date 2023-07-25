import translationLayer
import samplingSimulation
import deadtimeCalculator

BCM_min_bandpass = translationLayer.BCM_min_bandpass
BCM_bandpass_interval = translationLayer.BCM_bandpass_interval
BCM_max_bandpass = translationLayer.BCM_max_bandpass

BCM_storage = samplingSimulation.BCM_storage
length_deadtime_BCM = deadtimeCalculator.length_deadtime_BCM

epsilon_vs_BCM_resolution_array = []

def epsilon_vs_BCM_resolution(storage , seconds_in_wave , length_deadtime_detector):
    BCM_resolution = BCM_min_bandpass
    epsilon = 0
    while (BCM_resolution < BCM_max_bandpass):
        samplingSimulation.calc_wave_BCM(storage , seconds_in_wave , BCM_resolution)
        deadtimeCalculator.calc_length_deadtime_BCM(BCM_resolution)

        deadtime_false_asymmetry = len(length_deadtime_detector) - len(length_deadtime_BCM) #asymmetry resulting from mismatched deadtimes
        
        if (deadtime_false_asymmetry != 0):
            epsilon = deadtime_false_asymmetry #systematic error
        else:
            epsilon = deadtime_false_asymmetry #systematic error
        
        length_deadtime_BCM.clear()
        BCM_storage.clear()

        epsilon_vs_BCM_resolution_array.append(epsilon)
        BCM_resolution = BCM_resolution + BCM_bandpass_interval
    print('BCM Resolution vs. Systematic Error Finished')