import math
from math import pi
import constants

#transient simulation:
nominal_voltage_positve = constants.nominal_voltage_positve #positive nominal voltage of the wave, measured in volts
nominal_voltage_negative = constants.nominal_voltage_negative #negative nominal voltage of the wave, measured in volts
nominal_frequency_positive = constants.nominal_frequency_positive + constants.helicity_asymmetry #positive wave frequency, measured in hertz #helicity asymmetry added
nominal_frequency_negative = constants.nominal_frequency_negative #negative wave frequency, measured in hertz
voltage_ripple_positive = constants.voltage_ripple_positive #positive voltage ripple in the wave at nominal voltage, measured in volts
voltage_ripple_negative = constants.voltage_ripple_negative #negative voltage ripple in the wave at nominal voltage, measured in volts
transient_voltage_positive = constants.transient_voltage_positive #positive transient voltage of the wave, measured in volts
transient_voltage_negative = constants.transient_voltage_negative #negative transient voltage of the wave, measured in volts
transient_rt_voltage_positive = constants.transient_rt_voltage_positive #positive voltage of the rise time for the transient of the wave, measured in volts
transient_rt_voltage_negative = constants.transient_rt_voltage_negative #negative voltage of the rise time for the transient of the wave, measured in volts
transient_frequency_positive = constants.transient_frequency_positive + constants.helicity_asymmetry #positive transient frequency, measured in hertz #helicity asymmetry added
transient_frequency_negative = constants.transient_frequency_negative #negative transient frequency, measured in hertz
switching_frequency = constants.switching_frequency #switching frequency, measured in hertz

nominal_period_positive = 1 / nominal_frequency_positive #positive period of the wave, measured in seconds
nominal_period_negative = 1 / nominal_frequency_negative #negative period of the wave, measured in seconds
transient_period_positive = 1 / transient_frequency_positive #postive period of the transient, measured in seconds
transient_period_negative = 1 / transient_frequency_negative #negative period of the transient, measured in seconds
switching_period = 1 / switching_frequency #period of the switching, measured in seconds

nominal_angular_frequency_positive = int(nominal_frequency_positive * (2 * pi)) #positve angular frequency of the wave, measured in radians
nominal_angular_frequency_negative = int(nominal_frequency_negative * (2 * pi)) #negative angular frequency of the wave, measured in radians
transient_angular_frequency_positive = int(transient_frequency_positive * (2 * pi)) #positive angular frequency of the transient, measured in radians
transient_angular_frequency_negative = int(transient_frequency_negative * (2 * pi)) #negative angular frequency of the transient, measured in radians
switching_angular_frequency = int(switching_frequency * (2 * pi)) #angular frequency of the switching, measured in radians

#trigger pulse:
trigger_duty_cycle = constants.trigger_duty_cycle #duty cycle of the trigger pulse
trigger_nominal_voltage = constants.trigger_nominal_voltage #nominal voltage of the trigger pulse 
trigger_latency = constants.trigger_latency #latency of the trigger pulse ahead of the wave generation, measured in seconds
trigger_rise_time = constants.trigger_rise_time #period of the trigger pulse rise time, measured in seconds

#general:
num_of_modules = constants.num_of_modules #number of wave modules
graph_time_interval = constants.graph_time_interval #interval for the x-axis on the graph, measured in seconds
generation_resolution = constants.generation_resolution #resolution with which the wave is generated, measured in radians

#timer:
timer_lower_bound = constants.timer_lower_bound #lower bound to cut off the wave generation, measured in seconds
timer_upper_bound = constants.timer_upper_bound #upper bound to cut off the wave generation, measured in seconds

#sampling:
BCM_resolution = 1 / constants.BCM_resolution #frequency with which the BCM measures the wave aka samples per second, measured in hertz

#timing gates:
deadtime_width_BCM = constants.deadtime_width_BCM #factor by which the deadtime of the BCM is widened or thinned; thinner is negative, wider is positive; 1 for normal
deadtime_shift_BCM = constants.deadtime_shift_BCM #factor by which the deadtime of the BCM is moved left or right; left is negative, right is positive; measured in seconds

deadtime_width_detector = constants.deadtime_width_detector #factor by which the deadtime of the detector is widened or thinned; thinner is negative, wider is positive; 1 for normal
deadtime_shift_detector = constants.deadtime_shift_detector #factor by which the deadtime of the detector is moved left or right; left is negative, right is positive; measured in seconds

#asymmetry:
helicity_asymmetry = constants.helicity_asymmetry #asymmetry from the Moller collisions

BCM_min_bandpass = constants.BCM_min_bandpass #should be the same as the BCM's current maximum bandpass
BCM_bandpass_interval = constants.BCM_bandpass_interval #interval by which the bandpass of the BCM increases during systematic error calculations
BCM_max_bandpass = constants.BCM_max_bandpass #should be the theoretical maximum for the BCM's bandpass