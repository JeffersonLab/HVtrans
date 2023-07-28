#transient simulation:
nominal_voltage_positve = 3000 #positve nominal voltage of the power circuitry, measured in volts
nominal_voltage_negative = 3000 #negative nominal voltage of the power circuitry, measured in volts
nominal_frequency_positive = 500000 #positive nominal frequency of the power circuitry, measured in hertz
nominal_frequency_negative = 500000 #negative nominal frequency of the power circuitry, measured in hertz
voltage_ripple_positive = 600 #voltage ripple of the power circuitry, measured in volts
voltage_ripple_negative = 600 #voltage ripple of the power circuitry, measured in volts
transient_voltage_positive = 11400 #voltage of the transient, measured in volts
transient_voltage_negative = 11400 #voltage of the transient, measured in volts
transient_rt_voltage_positive = 17400 #voltage of the transient, measured in volts
transient_rt_voltage_negative = 17400 #voltage of the transient, measured in volts
transient_frequency_positive = 98039 #positive frequency of the transient, measured in hertz
transient_frequency_negative = 98039 #negative frequency of the transient, measured in hertz
switching_frequency = 1920 #switching frequency of the power circuitry, measured in hertz

# trigger pulse:
trigger_duty_cycle = 0.25 #duty cycle of the trigger pulse
trigger_nominal_voltage = 5 #nominal voltage of the trigger pulse
trigger_latency = 0 #latency of the trigger pulse ahead of the wave generation, measured in seconds
trigger_rise_time = 0.00001 #period of the trigger pulse rise time, measured in seconds

#general:
generation_resolution = 0.0000000001 #resolution with which the wave is generated, measured in radians #1 * 10^-9

num_of_modules = 2 #number of simulated voltage transistions
graph_time_interval = 0.0001 #interval for the x-axis on the graph, measured in seconds

#timer:
timer_lower_bound = 0 #lower bound to cut off the wave generation, measured in seconds
timer_upper_bound = 100000000000000000000000000000 #upper bound to cut off the wave generation, measured in seconds #1604.227 for one wave module

#sampling:
BCM_resolution = 150000 #frequency with which the BCM measures the wave (samples per second), measured in hertz #150000

#timing gates:
deadtime_width_BCM = 1 #factor by which the deadtime of the BCM is widened or thinned; thinner is <1, wider is >1; 1 for normal
deadtime_shift_BCM = 0 #factor by which the deadtime of the BCM is moved left or right; left is negative, right is positive; measured in seconds

deadtime_width_detector = 1 #factor by which the deadtime of the detector is widened or thinned; thinner is <1, wider is >1; 1 for normal
deadtime_shift_detector = 0 #factor by which the deadtime of the detector is moved left or right; left is negative, right is positive; measured in seconds

#asymmetry:
helicity_asymmetry = 0.000000033 #asymmetry from the MOLLER collisions #33 * 10^-9

BCM_bandpass_interval = 100000 #interval by which the bandpass of the BCM increases during systematic error calculations
BCM_max_bandpass = 1000000 #should be the theoretical maximum for the BCM's bandpass