import translationLayer
import transientSimulation
import BCMSimulation
import detectorSimulation

switching_period = translationLayer.switching_period
switching_angular_frequency = translationLayer.switching_angular_frequency
lower_bound_limit_radian = translationLayer.lower_bound_limit_radian
upper_bound_limit_radian = translationLayer.upper_bound_limit_radian

num_of_radian_per_module = switching_period * switching_angular_frequency

bcm = BCMSimulation.bcm
detector = detectorSimulation.detector

asymmetry = [] #list used for asymmetryCalculation

def calc_asymmetry(lower_bound , upper_bound , interval): #add a variable_to_vary and/or location_to_measure as potential parameters
    location_to_measure_radian = 5 #fixed location to measure in radians
    translationLayer.generation_resolution = lower_bound #set variable to iterate
    while (translationLayer.generation_resolution < upper_bound): #set variable to iterate
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

        translationLayer.generation_resolution += interval #set variable to iterate