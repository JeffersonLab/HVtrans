import translationLayer
import transientSimulation

generation_resolution = translationLayer.generation_resolution

storage = transientSimulation.storage

seconds_in_wave = len(storage) * generation_resolution #number of seconds in the entire generated wave

BCM_storage = [] #list used for BCM graph generation

def calc_wave_BCM(BCM_resolution): #samples the original wave at a rate equal to the BCM resolution to construct a new wave
    time1 = 0
    time2 = 0

    num_of_measurements_BCM = int(1 / BCM_resolution * seconds_in_wave) #number of measurements that the BCM takes of the original wave

    while (time1 < num_of_measurements_BCM):
        BCM_storage.append(storage[int(time2 / generation_resolution)])
        time2 = time2 + BCM_resolution
        time1 = time1 + 1