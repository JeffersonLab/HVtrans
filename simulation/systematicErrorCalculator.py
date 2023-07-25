import samplingSimulation
import deadtimeCalculator

epsilon_vs_BCM_resolution_array = []

def epsilon_vs_BCM_resolution(storage , generation_resolution , seconds_in_wave , length_deadtime_detector):
    BCM_resolution = 150000
    epsilon = 0
    while (BCM_resolution < 1000000):
        samplingSimulation.calc_wave_BCM(storage , seconds_in_wave , BCM_resolution)

        BCM_storage = samplingSimulation.BCM_storage

        deadtimeCalculator.calc_length_deadtime_BCM(BCM_resolution)

        length_deadtime_BCM = deadtimeCalculator.length_deadtime_BCM

        deadtime_false_asymmetry = len(length_deadtime_detector) - len(length_deadtime_BCM) #asymmetry resulting from mismatched deadtimes
        
        if (deadtime_false_asymmetry != 0):
            epsilon = deadtime_false_asymmetry #systematic error
        else:
            epsilon = deadtime_false_asymmetry #systematic error
        
        length_deadtime_BCM.clear()
        BCM_storage.clear()

        epsilon_vs_BCM_resolution_array.append(epsilon)
        BCM_resolution = BCM_resolution + 10000
    print(':)')