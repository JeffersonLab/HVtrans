import translationLayer
import transientSimulation

nominal_frequency_positive = translationLayer.nominal_frequency_positive
nominal_frequency_negative = translationLayer.nominal_frequency_negative

detector_sampling_rate = translationLayer.detector_sampling_rate
detector_frequency_cutoff = translationLayer.detector_frequency_cutoff
num_of_seconds_bounded = translationLayer.num_of_seconds_bounded
num_of_radians_bounded = translationLayer.num_of_radians_bounded
e = translationLayer.e

nominal_frequency_average = ((nominal_frequency_positive + nominal_frequency_negative) / 2)

detector = [] #list used for detectorSimulation generation

def calc_detector_frequency_response(frequency): #calculates a scalar multiplier for the detector resolution by a frequency vs. scalar multiplier curve, parameters frequency in hertz
    frequency_mhz = frequency / 1000000
    detector_frequency_cutoff_mhz = detector_frequency_cutoff / 1000000
    multiplier = (-1 / pow(e , (-frequency_mhz + detector_frequency_cutoff_mhz))) + 1 #decay funtion to determine the detector frequency response, currently (-1 / (e ^ (-x + frequency_cutoff))) + 1 where x is in megahertz and probability is a decimal between zero and one
    return multiplier

def calc_detector():
    num_of_calcs = calc_detector_frequency_response(nominal_frequency_average) * num_of_seconds_bounded * detector_sampling_rate #number of detector measurements over bounded interval
    detector_resolution = num_of_radians_bounded / num_of_calcs #detector resolution in radians
    time = 0
    while(time < int(num_of_radians_bounded)):
        detector.append(transientSimulation.read_current_amplitude(time))
        time = time + detector_resolution

def read_current_amplitude(radian_location): #returns the current amplitude of the bcm at a given radian location, parameter radian_location in radians
    detector_resolution = num_of_radians_bounded / len(detector)
    current_amplitude = detector[int(radian_location / detector_resolution)]
    return current_amplitude