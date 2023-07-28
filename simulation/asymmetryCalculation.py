import translationLayer
import transientSimulation
import BCMSimulation
import detectorSimulation

num_of_radian_per_module = translationLayer.num_of_radian_per_module
lower_bound_limit_radian = translationLayer.lower_bound_limit_radian
upper_bound_limit_radian = translationLayer.upper_bound_limit_radian

bcm = BCMSimulation.bcm
detector = detectorSimulation.detector

asymmetry = [] #list used for asymmetryCalculation

def calc_asymmetry(lower_bound , upper_bound , interval): #add a variable_to_vary and/or location_to_measure as potential parameters
    location_to_measure_radian = 5 #fixed location to measure in radians
    translationLayer.detector_sampling_rate = lower_bound #set variable to iterate
    while (translationLayer.detector_sampling_rate < upper_bound): #set variable to iterate
        transientSimulation.calc_wave(lower_bound_limit_radian , upper_bound_limit_radian)
        BCMSimulation.calc_bcm()
        detectorSimulation.calc_detector()

        d_plus = BCMSimulation.read_current_amplitude(location_to_measure_radian)
        d_minus = BCMSimulation.read_current_amplitude(location_to_measure_radian + num_of_radian_per_module)
        b_plus = detectorSimulation.read_current_amplitude(location_to_measure_radian)
        b_minus = detectorSimulation.read_current_amplitude(location_to_measure_radian + num_of_radian_per_module)
        d_plus_div_b_plus = d_plus / b_plus
        d_minus_div_b_minus = d_minus / b_minus
        total_asymmetry = (d_plus_div_b_plus - d_minus_div_b_minus) / (d_plus_div_b_plus + d_minus_div_b_minus)
        asymmetry.append(total_asymmetry)

        translationLayer.detector_sampling_rate += interval #set variable to iterate

def read_current_asymmetry(parameter_value, lower_bound , upper_bound , interval):
    index = int((parameter_value / interval) - (lower_bound / interval))
    current_asymmetry = asymmetry[index]
    return current_asymmetry