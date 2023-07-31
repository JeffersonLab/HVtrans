import translationLayer
import transientSimulation

nominal_frequency_positive = translationLayer.nominal_frequency_positive
nominal_frequency_negative = translationLayer.nominal_frequency_negative
nominal_frequency_average = translationLayer.nominal_frequency_average

bcm_sampling_rate = translationLayer.bcm_sampling_rate
bcm_frequency_cutoff = translationLayer.bcm_frequency_cutoff
num_of_seconds_bounded = translationLayer.num_of_seconds_bounded
num_of_radians_bounded = translationLayer.num_of_radians_bounded
e = translationLayer.e

bcm = [] #list used for BCMSimulation generation

def calc_bcm_frequency_response(frequency): #calculates a scalar multiplier for the beam current monitor resolution by a frequency vs. scalar multiplier curve, parameters frequency in hertz
    frequency_mhz = frequency / 1000000
    bcm_frequency_cutoff_mhz = bcm_frequency_cutoff / 1000000
    multiplier = (-1 / pow(e , (-frequency_mhz + bcm_frequency_cutoff_mhz))) + 1 #decay funtion to determine the beam current monitor frequency response, currently (-1 / (e ^ (-x + frequency_cutoff))) + 1 where x is in megahertz and probability is a decimal between zero and one
    return multiplier

def calc_bcm(): #calculates the beam current monitor graph by reading from the transientSimulation array according to bcm_resolution
    num_of_calcs = calc_bcm_frequency_response(nominal_frequency_average) * num_of_seconds_bounded * bcm_sampling_rate #number of beam current monitor measurements over bounded interval
    bcm_resolution = num_of_radians_bounded / num_of_calcs #beam current monitor resolution in radians
    time = 0
    while(time < int(num_of_radians_bounded)):
        bcm.append(transientSimulation.read_current_amplitude(time))
        time = time + bcm_resolution

def read_current_amplitude(radian_location): #returns the current amplitude of the bcm at a given radian location, parameter radian_location in radians
    bcm_resolution = num_of_radians_bounded / len(bcm)
    current_amplitude = bcm[int(radian_location / bcm_resolution)]
    return current_amplitude