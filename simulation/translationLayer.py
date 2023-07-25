import math
from math import pi
import constants

#transient simulation:
resistance = constants.resistance
capacitance = constants.capacitance

nominal_voltage_positve = constants.nominal_voltage_positve #positive nominal voltage of the wave, measured in volts
nominal_voltage_negative = constants.nominal_voltage_negative #negative nominal voltage of the wave, measured in volts
nominal_frequency_positive = constants.nominal_frequency_positive #positive wave frequency, measured in hertz
nominal_frequency_negative = constants.nominal_frequency_negative #negative wave frequency, measured in hertz
voltage_ripple_positive = constants.voltage_ripple_positive #positive voltage ripple in the wave at nominal voltage, measured in volts
voltage_ripple_negative = constants.voltage_ripple_negative #negative voltage ripple in the wave at nominal voltage, measured in volts
transient_voltage_positive = constants.transient_voltage_positive #positive transient voltage of the wave, measured in volts
transient_voltage_negative = constants.transient_voltage_negative #negative transient voltage of the wave, measured in volts
transient_frequency_positive = constants.transient_frequency_positive #positive transient frequency, measured in hertz
transient_frequency_negative = constants.transient_frequency_negative #negative transient frequency, measured in hertz
switching_frequency = constants.switching_frequency #switching frequency, measured in hertz
time_constant = resistance * capacitance #value to determine the rate of transient decay, full decay occurs after five time constants, measured in seconds

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

transient_rise_time_positive = constants.transient_rise_time_positive #positve transient rise time, measured in seconds
transient_rise_time_negative = constants.transient_rise_time_negative #negative transient rise time, measured in seconds
transient_rise_time_radian_positive = transient_rise_time_positive * nominal_angular_frequency_positive #positive transient rise time, converted to radians according to the nominal angular frequency
transient_rise_time_radian_negative = transient_rise_time_negative * nominal_angular_frequency_negative #negative transient rise time, converted to radians according to the nominal angular frequency

#general:
num_of_phases_positive = (switching_period - transient_period_positive) / nominal_period_positive #positive number of nominal phases per wave module
num_of_phases_negative = (switching_period - transient_period_negative) / nominal_period_negative #negative number of nominal phases per wave module
num_of_phases = num_of_phases_positive + num_of_phases_negative #total number of phases throughout all modules
num_of_modules = constants.num_of_modules #number of wave modules
num_of_modules_positive = round(num_of_modules / 2) #number of positive modules
num_of_modules_negative = int(num_of_modules / 2) #number of negative modules
generation_resolution = constants.generation_resolution #resolution with which the wave module is generated, measured in radians
graph_time_interval = constants.graph_time_interval #interval for the x-axis on the graph, measured in seconds
lower_bound_limit = constants.lower_bound_limit #horizontal lower bound limit of the graph, measured in seconds
upper_bound_limit = constants.upper_bound_limit #horizontal upper bound limit of the graph, measured in seconds
lower_bound_limit_radian = lower_bound_limit * switching_angular_frequency #0 #horizontal lower bound limit of the graph, measured in radians
upper_bound_limit_radian = upper_bound_limit * switching_angular_frequency #2000 #horizontal upperr bound limit of the graph, measured in radians

num_of_seconds_positive = (num_of_modules_positive * switching_period) + (num_of_modules_negative * transient_rise_time_positive) #number of seconds during positve modules
num_of_seconds_negative = (num_of_modules_negative * switching_period) + ((num_of_modules_positive - 1) * transient_rise_time_negative) #number of seconds during negative modules
num_of_seconds = num_of_seconds_positive + num_of_seconds_negative #total number of seconds throughout all modules
num_of_seconds_bounded = upper_bound_limit - lower_bound_limit #number of seconds in the bounded wave
num_of_radians_bounded = upper_bound_limit_radian - lower_bound_limit_radian #number of radians in the bounded wave

#trigger pulse:
trigger_duty_cycle = constants.trigger_duty_cycle #duty cycle of the trigger pulse
trigger_nominal_voltage = constants.trigger_nominal_voltage #nominal voltage of the trigger pulse 
trigger_latency = constants.trigger_latency #latency of the trigger pulse ahead of the wave generation, measured in seconds
trigger_rise_time = constants.trigger_rise_time #period of the trigger pulse rise time, measured in seconds
trigger_radian_rise_time = trigger_rise_time * switching_angular_frequency #period of the trigger pulse rise time, measured in radians

#BCM Simulation:
bcm_sampling_rate = constants.bcm_sampling_rate #sampling rate of the beam current monitor, measured in samples per second
bcm_frequency_cutoff = constants.bcm_frequency_cutoff #beam current monitor frequency cutoff, measured in hertz

#Detector Simulation:
detector_sampling_rate = constants.detector_sampling_rate #sampling rate of the detector, measured in samples per second
detector_frequency_cutoff = constants.detector_frequency_cutoff #detector frequency cutoff, measured in hertz

#Deadtime Simulation:
gate_timing_lower_bound = constants.gate_timing_lower_bound #expected lower bound of the deadtime, measured in seconds
gate_timing_upper_bound = constants.gate_timing_upper_bound #expected length of the deadtime, measured in seconds
gate_timing_bound_offset = constants.gate_timing_bound_offset #offset in the deadtime lower bound, measured in seconds
gate_timing_length_offset = constants.gate_timing_length_offset #offset in the deadtime length, measured in seconds
gate_timing_length = gate_timing_upper_bound - gate_timing_lower_bound

#constants:
e = 2.71828 #18284590452353602874713527 #euler's number constant